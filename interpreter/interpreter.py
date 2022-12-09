def main():
    expression = input("Enter your expression").strip()
    print(cal(expression))





def cal(e):
    x, y, z = e.split(" ")
    x = int(x)
    z = int(z)
    if y == "*":
        return float(x * z)
    elif y == "-":
        return float(x - z)
    elif y == "+":
        return float(x + z)
    else:
        return float(x / z)




if __name__ == "__main__":
    main()