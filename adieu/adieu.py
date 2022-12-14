import sys





names = []
while True:
    try:
        name = input("Name: ")
    except EOFError:
        for name in names:
        print("Adieu, adieu, to", )
        sys.exit()
