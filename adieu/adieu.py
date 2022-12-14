import sys





names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        print("")
        sys.exit()
    