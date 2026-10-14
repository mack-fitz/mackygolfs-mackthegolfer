#!/usr/bin/env python3
"""Video fingerprints for the duplicate check (DUPLICATE CHECK V2 in PLAYBOOK.md).

  python3 tools/fingerprint.py video  <file> <out.json> [--meta k=v ...]
  python3 tools/fingerprint.py image  <file> <out.json> [--meta k=v ...]   (thumbnail fallback)

Output JSON (small, safe to commit; never commit the videos themselves):
  {"kind": "video"|"thumbnail", "duration": s,
   "audio": {"item_s": 0.1238, "fp": [uint32 ...]}            # chromaprint (fpcalc -raw)
   "frames": [[t, "phash16hex"], ...]                          # perceptual hash every 2 s
   "frames_dense": [[t, "phash16hex"], ...]                    # every 0.5 s (sources only, --dense)
   "meta": {...}}
Needs: fpcalc (libchromaprint-tools), ffmpeg/ffprobe, pip imagehash pillow.
"""
import json, os, subprocess, sys, tempfile, glob

def phash_file(p):
    import imagehash
    from PIL import Image
    im = Image.open(p).convert("L")
    w, h = im.size
    # centre crop to the middle 80% so small punch-ins / UI crops hurt less
    im = im.crop((int(w * .1), int(h * .1), int(w * .9), int(h * .9)))
    return str(imagehash.phash(im, hash_size=8))

def duration(path):
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                              "-of", "default=nw=1:nk=1", path], capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout
        return round(float(out.strip()), 2)
    except Exception:
        return None

def audio_fp(path):
    r = subprocess.run(["fpcalc", "-raw", "-json", "-length", "0", path], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0 or not r.stdout.strip():
        return None
    d = json.loads(r.stdout)
    fp = d.get("fingerprint") or []
    return {"item_s": 0.1238, "fp": [int(x) & 0xFFFFFFFF for x in fp]}

def frames(path, step):
    out = []
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-i", path, "-vf",
                        f"fps=1/{step},scale=160:-2", os.path.join(td, "f%05d.png")], check=False, stdin=subprocess.DEVNULL)
        for i, f in enumerate(sorted(glob.glob(os.path.join(td, "f*.png")))):
            # fps filter samples the frame at the middle of each interval
            out.append([round(i * step + step / 2, 2), phash_file(f)])
    return out

def main():
    mode, src, dst = sys.argv[1:4]
    args = sys.argv[4:]
    meta, dense = {}, False
    for a in args:
        if a == "--dense":
            dense = True
        elif "=" in a:
            k, v = a.split("=", 1); meta[k] = v
    if mode == "video":
        res = {"kind": "video", "duration": duration(src), "audio": audio_fp(src),
               "frames": frames(src, 2.0)}
        if dense:
            res["frames_dense"] = frames(src, 0.5)
    else:
        res = {"kind": "thumbnail", "duration": None, "audio": None,
               "frames": [[0, phash_file(src)]]}
    res["meta"] = meta
    os.makedirs(os.path.dirname(dst) or ".", exist_ok=True)
    json.dump(res, open(dst, "w"), separators=(",", ":"))
    print(dst, res["kind"], res["duration"], len((res["audio"] or {}).get("fp", [])), len(res["frames"]))

if __name__ == "__main__":
    main()
