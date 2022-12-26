from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    print(how_many_minutes(input("Date of Birth: ")))


def how_many_minutes(s):
    try:
        s = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")
    s = (date.today() - s)
    s =  int(s.total_seconds() / 60)
    return p.number_to_words(s, andword="") + " minutes"




if __name__ == "__main__":
    main()