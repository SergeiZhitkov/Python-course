import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if s := re.search(r"^(1[0-2]|1[0-2]:[0-5][0-9]|[1-9]|) (am|pm) to (1[0-2]|[1-9])(am|pm)$", s, flags=re.IGNORECASE):
        return
    else:
        raise ValueError





if __name__ == "__main__":
    main()