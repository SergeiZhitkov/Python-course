def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return f"{d:.1f}"


def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p)
    return f"{(p / 100):.2f}"

if __name__ == "__main__":
    main()