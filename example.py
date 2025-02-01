import requests

r = requests.get('https://api.nbp.pl/api/exchangerates/rates/a/usd?format=json')
print(r.json())