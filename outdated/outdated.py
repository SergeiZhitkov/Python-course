

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
    try:
        date = input("Date: ").strip().lower()
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            if 0 < month < 13:
                if 0 < day < 32:
                    print(f"{year}-{month:02}-{day:02}")
                    break
    except ValueError:
        pass
    try:
        month, day, year = date.split(" ")
        month = months[month]
        day = day.replace(",", "")
        day = int(day)
        if 0 < day < 32:
            print(f"{year}-{}")
    except (ValueError, KeyError):
        pass
