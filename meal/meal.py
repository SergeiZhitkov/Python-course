def main():
    time = input("What's time? ").strip()
    print(convert(time))

def convert(t):
    hour, minut = t.split(":")
    hour = float(hour)
    minut = float(minut) / 60
    t = hour + minut
    if 7 <= t <= 8:
        return "breakfast time"
    elif 12 <= t <= 13:
        return "lunch time"
    elif 18 <= t <= 19:
        return "dinner time"
    

if __name__ == "__main__":
    main()