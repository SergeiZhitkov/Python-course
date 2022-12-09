def main():
    time = input("What's time? ").strip()
    if 7 <= convert(time) <= 8:
        print("breakfast time")
    elif 12 <= convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) <= 19:
        print("dinner time")

def convert(t):
    hour, minut = t.split(":")
    hour = float(hour)
    minut = float(minut) / 60
    return hour + minut


if __name__ == "__main__":
    main()