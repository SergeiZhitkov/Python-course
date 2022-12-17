def main():
    fraction = input("Fraction: ").strip()
    fraction = percentage(fraction)
    if fraction >= 99:
        print("F")
    elif fraction <= 1:
        print("E")
    else:
        print(f"{fraction:.0f}%")

def percentage(f):
    while True:
        try:
            x, y = f.split("/")
            x = int(x)
            y = int(y)
            if x <= y and y != 0:
                return float(x) / float(y) * 100
        except (ValueError, ZeroDivisionError):
            f = input("Fraction: ").strip()
            pass







if __name__ == "__main__":
    main()

