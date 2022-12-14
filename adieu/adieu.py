import sys





names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        if len(names) == 1:
            print(f"\nAdieu, adieu, to {name}")
            sys.exit()
        elif len(names) == 2:
            print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")
            sys.exit()
        else:
            print("\nAdieu, adieu, to ", end="")
            for name in names[:-1]:
                print(f"{name}, ", end="")
            print(f"and {names[len(names)-1]}")
            sys.exit()
    names.append(name)