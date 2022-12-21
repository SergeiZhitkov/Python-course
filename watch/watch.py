import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s := re.search(r'"https?(?:www\.)?://youtube\.com/embed/(\w)"$', s, flag=RE.IGNORCASE):
        return s
    else:
        sys.exit("")




if __name__ == "__main__":
    main()