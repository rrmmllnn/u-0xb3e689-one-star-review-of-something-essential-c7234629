"""A one-star review of an essential thing: the sun."""
import os
import sys


def build_review():
    praise = "The sun provides free light and warmth every day, then "
    gripe = "sunburns the one square inch of skin I forgot to cover."
    return "".join([praise, gripe])


def main():
    review = build_review()
    size = len(review)
    if not 1 <= size <= 160:
        sys.stderr.write("bad review length: %d (want 1-160)\n" % size)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8", newline="") as out:
        out.write(review)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
