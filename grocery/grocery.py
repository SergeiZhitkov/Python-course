import sys
items = {}
while True:
    try:
        item = input("").lower().strip()
    except EOFError:
        for key, value in sorted(items.items()):
            print(value, key.upper())
        sys.exit()
    try:
        if items[item]:
            items[item] += 1
    except KeyError:
        items[item] = 1