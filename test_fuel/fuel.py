import sys

def main():
    fraction = input("Fraction: ").strip()
    fraction = convert(fraction)
    print(gauge(fraction))


def convert(f):
    x, y = f.split("/")
    x = int(x)
    y = int(y)
    if x <= y :
        return int(float(x) / float(y) * 100)
    else:
        raise(ValueError)

def gauge(fraction):
    if fraction >= 99:
            return("F")
    elif fraction <= 1:
            return("E")
    else:
            return(f"{fraction:.0f}%")







if __name__ == "__main__":
    main()

