import argparse
import re

BEGIN_END_PAIRS = [
    (r"#\s*BEG\s*SOLUTION", r"#\s*END\s*SOLUTION"),
    (r"#\s*BEG\s*HIDDEN\s*TESTS", r"#\s*END\s*HIDDEN\s*TESTS"),
]


def strip_blocks(lines):
    begin_regexes = [re.compile(b) for b, _ in BEGIN_END_PAIRS]
    end_regexes = [re.compile(e) for _, e in BEGIN_END_PAIRS]

    inside_block = False
    active_pair_idx = None
    out = []

    for line in lines:
        if not inside_block:
            for i, beg in enumerate(begin_regexes):
                if beg.search(line):
                    inside_block = True
                    active_pair_idx = i
                    break
            else:
                out.append(line)
        else:
            if end_regexes[active_pair_idx].search(line):
                inside_block = False
                active_pair_idx = None

    return out


def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = strip_blocks(lines)

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Remove solution and hidden-test cases from their respective scripts"
    )
    parser.add_argument("files", nargs="+", help="Scripts to update in-place")
    args = parser.parse_args()

    for path in args.files:
        process_file(path)


if __name__ == "__main__":
    main()
