import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "sentiment/1", {"name": "Carlos", "review": "El sitio es maravilloso"})
print(response.json())

response = requests.post(BASE + "sentiment/1")
print(response.json())