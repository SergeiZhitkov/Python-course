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
# print(json.dumps(response.json(), indent=2))
response = response.json()
result = float(response["bpi"]["USD"]["rate_float"])
print(f"${result * value:,.4f}")
#for valute in response["bpi"]:
 #   print()