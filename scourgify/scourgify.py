import csv
import sys

new_file = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            first, last = row["name"].split(", ")
            new_file.append({"first" : first, "last" : last, "house" : house})
except FileNotFoundError:
    sys.exit("File does not exist")

with open("after.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=)
    for row in writer:
