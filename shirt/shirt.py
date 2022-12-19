import sys
import csv
from PIL import Image

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

for file in sys.argv[1:]:
    if file != file.endswith(".jpeg") and file != file.endswith(".png")
        sys.exit("")

try:
    with Image.open(sys.argv[1]) as file:
        