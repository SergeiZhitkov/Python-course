import re
import sys

time = {
    "am" : {
        "12" : "00",
        "1" : "01",
        "2" : "02",
        "3" : "03",
        "4" : "04",
        "5" : "05",
        "6" : "06",
        "7" : "07",
        "8" : "08",
        "9" : "09",
        "10" : "10",
        "11" : "11",
    },
    "pm" : {
        "12" : "12",
        "1" : "13",
        "2" : "14",
        "3" : "15",
        "4" : "16",
        "5" : "17",
        "6" : "18",
        "7" : "19",
        "8" : "20",
        "9" : "21",
        "10" : "22",
        "11" : "23",
    }


}


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|1[0-2]:[0-5][0-9]|[1-9]|[1-9]:[0-5][0-9]) (am|pm) to (1[0-2]|1[0-2]:[0-5][0-9]|[1-9]|[1-9]:[0-5][0-9]) (am|pm)$", s.strip(), flags=re.IGNORECASE):
        try:
            hour, minute = matches.group(1).split(":")
            hour = time[matches.group(2)][hour]
        except ValueError:
            pass
        


        matches.group(3)
        matches.group(4)

    else:
        raise ValueError





if __name__ == "__main__":
    main()