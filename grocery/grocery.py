import sys
items = {}
while True:
    try:
        item = input("").lower().strip()
    except EOFError:
        for key, value in items.items():
            print(value, item.upper())
        sys.exit()
    try:
        if items[item]:
            items[item] += 1
    except KeyError:
        items[item] = 1