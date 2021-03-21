import requests

BASE = "http://127.0.0.1:5000/"

videos = [{"name": "parrot sings and flies across the room", "likes": 94, "views": 2042}]

response = requests.get(BASE + "/videos")
print(response.json())

response = requests.put(BASE + "/videos/1", videos[0])
print(response.json())

response = requests.get(BASE + "/videos/1")
print(response)
print(response.json())

response = requests.get(BASE + "/videos/1")
print(response.json())

requests.delete(BASE + "/videos/1")
print(response.json())

response = requests.get(BASE + "/videos/1")
print(response.json())
