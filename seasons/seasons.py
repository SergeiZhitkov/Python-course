from datetime import date
import sys

def main():
    print(how_many_minutes(input("Date of Birth: ")))



def how_many_minutes(s):
    try:
        s = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")
    s = (date.today() - s) * 24 * 60
    return s.total_seconds() / 60
   




if __name__ == "__main__":
    main()