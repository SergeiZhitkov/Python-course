import sys





names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print("Adieu, adieu, to ", end="")
        for name in names[:-1]:
            print(f"{name},", end="")
        print(f"and {names[len(names)-1]}")
        sys.exit()
    names.append(name)