import requests 

response = requests.get("https://api.npoint.io/d9fb8e234a2738238e84")
api_data = response.json()
titles, subtitles, bodies = [api_data[i]["title"] for i in range(3)], [api_data[i]["subtitle"] for i in range(3)], [api_data[i]["body"] for i in range(3)]

print(titles[0])
