import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"^(\w+\W+||\W+)um(\W+\w*|)$", s, re.IGNORECASE)
    return len(matches)



if __name__ == "__main__":
    main()