import requests
import sys
import json


try:
    value = (sys.argv[1])
    value = float(value)
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

respond = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(json.dumps(respond.json()))