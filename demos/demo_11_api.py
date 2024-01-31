import requests

url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"

my_filter = {"merk": "TESLA"}

r = requests.get(url, params=my_filter)

print(r)
