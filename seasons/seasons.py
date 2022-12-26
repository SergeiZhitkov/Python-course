from datetime import date
import sys

def main():
    print(how_many_minutes(input("Date of Birth: ")))



def how_many_minutes(s):
    year, month, day = s.split("-")
    year = int(year)




if __name__ == "__main__":
    main()