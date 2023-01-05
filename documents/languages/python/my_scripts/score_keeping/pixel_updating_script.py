import requests

#endpoint customized to update the recently created graph, it contains the graph id in its path URL.
endpoint = "https://pixe.la/v1/users/mauboro/graphs/pomokiller"
TOKEN = "lkjdfhaoiuhhrf9183475y134iuh31oifjbqer8fu"

#creates the parameters needed to populate the HTTP post request with the required options for the pixel insertion.
graph_params = {
    "token": TOKEN, 
    "unit": "commit",
    "date": "20221227",
    "quantity": "0" 
}

#creates a dict(just like the graph_params dict) to store required info for the header of request.
headers = {
    "X-USER-TOKEN": TOKEN
}

#a post request again.
response = requests.post(url=endpoint, headers=headers, json=graph_params)
print(response.json())
