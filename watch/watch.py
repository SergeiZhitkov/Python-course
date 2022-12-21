import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s := re.search(r'.+"https?(?:www\.)?://youtube\.com/embed/(\w)".+', s, flags=re.IGNORECASE):
        return s
    else:
        return None




if __name__ == "__main__":
    main()