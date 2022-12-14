import requests
import sys

try:
    value = (sys.argv[1])
except (IndexError):
    sys.exit("Missing command-line argument")
try:
    value = float(value)
except ValueError:
    sys.exit("Command-line argument is not a number")