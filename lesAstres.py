import requests

url = "https://api.le-systeme-solaire.net/rest/bodies/?data=id,semimajorAxis,isPl&exclude=id,isPlanet&order=semimajorAxis,asc&page=1,10&rowData=true"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)