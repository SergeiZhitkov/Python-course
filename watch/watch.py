import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = re.search(r".+\"https?(?:www\.)?://youtube\.com/embed/(\w+)\".+", s, flags=re.IGNORECASE)
    return s



if __name__ == "__main__":
    main()