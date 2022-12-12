

months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
    ]
while True:
    date = input("Date: ").strip().lower()
    if "/" in date:
        try:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
        except ValueError:
            pass
        if 0 < month < 13:
            if 0 < day < 32:
                print(f"{year}-{month:02}-{day:02}")
                break
    month, day, year = date.split(" ")
    month