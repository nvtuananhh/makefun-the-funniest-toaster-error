# Toaster error entry — final version (revised punchline)
# Writes a single funny toaster error line to entry.txt.
import os

ENTRY = "ERROR: No bread detected. I toasted the air for three minutes and it still left me on read."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

if __name__ == "__main__":
    main()
