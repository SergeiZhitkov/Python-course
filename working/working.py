import re
import sys

time = {
    "am" : {
        12
    }


}


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|1[0-2]:[0-5][0-9]|[1-9]|[1-9]:[0-5][0-9]) (am|pm) to (1[0-2]|1[0-2]:[0-5][0-9]|[1-9]|[1-9]:[0-5][0-9]) (am|pm)$", s.strip(), flags=re.IGNORECASE):
        if matches.group(2) == "am":

        matches.group(3)
        matches.group(4)

    else:
        raise ValueError





if __name__ == "__main__":
    main()