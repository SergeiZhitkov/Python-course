from datetime import date
import sys

def main():
    print(how_many_minutes(input("Date of Birth: ")))



def how_many_minutes(s):
    try:
        year, month, day = int(s.split("-"))
    except ValueError:
        sys.exit("Invalid date")
    s = 



if __name__ == "__main__":
    main()