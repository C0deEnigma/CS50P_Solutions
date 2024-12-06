import sys
import requests
try:
    response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    o=response.json()
    d=o['bpi']['USD']['rate_float']
    amount=float(sys.argv[1])*d
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')
