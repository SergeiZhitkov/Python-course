import sys
items = [
]
while True:
    try:
        item = input("").lower().strip()
    except EOFError:
        sys.exit()
    items[item] = 1
    print(items[item])