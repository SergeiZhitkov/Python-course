import requests
import sys


if len(sys.argv) != 2:
    sys.exit()
try:
    value = float(sys.argv[1])
except ValueError:
    sys.exit()