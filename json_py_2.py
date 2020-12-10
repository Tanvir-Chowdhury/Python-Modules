import json
from urllib.request import urlopen

with urlopen("http://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)
print(json.dumps(data, indent=4))