def main():
    fraction = input("Fraction: ").strip()
    percentage(fraction)
    print(f"{fraction}%")


def percentage(f):
    while True:
        try:
            x, y = f.split("/")
            x = int(x)
            y = int(y)
            if x <= y and y != 0:
                return float(x)/float(y) * 100
        except (ValueError, ZeroDivisionError):
            f = input("Fraction: ").strip()
            pass







if __name__ == "__main__":
    main()


