import requests
from sys import argv, exit

if len(argv) != 2:
    exit("Missing command-line argument.")
try:
    number = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number.")

try:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except requests.RequestException:
    exit("There was an Error while handling your request.")
else:
    print(f"${request["bpi"]["USD"]["rate_float"] * number:,.4f}")
