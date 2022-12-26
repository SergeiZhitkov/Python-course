from datetime import date
import sys
import inflect

def main():
    print(how_many_minutes(input("Date of Birth: ")))



def how_many_minutes(s):
    try:
        s = date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")
    s = (date.today() - s) * 24 * 60
    s =  s.total_seconds() / 60
    return s.number_to_words(1234, andword="")




if __name__ == "__main__":
    main()