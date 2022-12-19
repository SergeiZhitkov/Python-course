import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

for file in sys.argv[1:]:
    if file != file.endswith(".jpeg") and file != file.endswith(".png")
        sys.exit("")