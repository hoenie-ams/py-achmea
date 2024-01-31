import requests


data = []


def fetch(url):
    r = requests.get(url, params={"state": "open"})
    print("Fetching:", r.url)
    return r


url = "https://api.github.com/repos/ansible/ansible/issues"


while True:
    result = fetch(url)
    links = result.links
    data.extend(result.json())

    if links.get("next"):
        url = links["next"]["url"]
    else:
        break


for record in data:
    print(record["title"])

