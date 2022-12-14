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

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
# print(json.dumps(response.json(), indent=2))
for result in o["bpi"]:
    print(result['rate'])