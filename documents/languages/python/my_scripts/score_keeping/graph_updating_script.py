import requests

#endpoint customized to update the recently created graph, it contains the graph id in its path URL.
endpoint = "https://pixe.la/v1/users/mauboro/graphs/pomokiller"
TOKEN = "lkjdfhaoiuhhrf9183475y134iuh31oifjbqer8fu"

#creates the parameters needed to populate the HTTP post request with the required options for the graph creation.
graph_params = {
    "token": TOKEN, 
    "color": "shibafu"
}

#creates a dict(just like the graph_params dict) to store required info for the header of request.
headers = {
    "X-USER-TOKEN": TOKEN
}

#now the request was altered to be a put request instead of a post one, to propery update the file. don't ask me why, I'm sleepy.
response = requests.put(url=endpoint, headers=headers, json=graph_params)
print(response.json())
