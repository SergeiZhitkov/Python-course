import csv
import sys

new_file = []

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
if sys.argv[2].endswith(".csv") == False:
    sys.argv[2] = sys.argv[2] + ".csv"

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(", ")
            new_file.append({"first" : first, "last" : last, "house" : row["house"]})
except FileNotFoundError:
    sys.exit("File does not exist")

with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writerow({"first" : "first", "last": "last", "house": "house"})
    for row in new_file:
        writer.writerow({"first" : row["first"], "last" : row["last"], "house" : row["house"]})
