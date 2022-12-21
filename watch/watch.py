import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s := re.search(r"https?(ww\.)?://youtube.com/embed/", s, flag=RE.IGNORCASE):





if __name__ == "__main__":
    main()