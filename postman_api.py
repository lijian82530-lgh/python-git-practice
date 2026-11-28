"""import requests

url = ("http://fruityvice.com(api/fruit/all")

response = request.get(url)
data = response.json()
ids = [fruit["id"] for fruit in data]

print(ids)"""


data = [
{"id": 1, "name": "Apple"},
{"id": 2, "name": "Banana"},
{"id": 3, "name": "Orange"}
]

for fruit in data:
    print(fruit["id"])