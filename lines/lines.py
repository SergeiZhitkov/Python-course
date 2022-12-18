import sys

if sys.argv > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv < 2:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")

with open(argv[1]) as file:
    reader = file.readlines()






