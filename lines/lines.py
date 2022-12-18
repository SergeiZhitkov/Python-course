import sys


strings = 0

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line != " " and line[0] != "#":
            strings += 1

print(strings)








