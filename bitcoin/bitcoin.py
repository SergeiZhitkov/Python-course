import requests
import sys

try:
    value = (sys.argv[1])
    value = float(value)
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

respond = request.get("https://api.coindesk.com/v1/bpi/currentprice.json")