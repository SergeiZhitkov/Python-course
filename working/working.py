import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if s := re.search(r"(1-9]) (am|pm)? to ()(am|pm)?$", s, flags=re.IGNORECASE):
        return
    else:
        raise ValueError





if __name__ == "__main__":
    main()