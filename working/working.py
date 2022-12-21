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
            first_hour, minutes = matches.group(1).split(":")
            first_hour = time[matches.group(2)][first_hour]
            first_hour = first_hour + ":" + minutes
        except ValueError:
            first_hour = time[matches.group(2)][first_hour]
            first_hour = first_hour + ":00"
            pass
        try:
            second_hour, minutes = matches.group(3).split(":")
            second_hour = time[matches.group(4)][second_hour]
            second_hour = second_hour + ":" + minutes
        except ValueError:
            second_hour = time[matches.group(4)][second_hour]
            second_hour = second_hour + ":00"
            pass
        return f"{first_hour} to {second_hour}"
    else:
        raise ValueError





if __name__ == "__main__":
    main()