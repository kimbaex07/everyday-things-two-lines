import os

LINE_1 = "A queue is a caterpillar made of people, each person one segment that shuffles forward only when the head moves."
LINE_2 = "It works because it maps the slow, linked shuffle of a line, but it leaves out the grumbling, the phone-checking, and the friends who cut in."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE_1 + "\n")
        f.write(LINE_2 + "\n")


if __name__ == "__main__":
    main()
