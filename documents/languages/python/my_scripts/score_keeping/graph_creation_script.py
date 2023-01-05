import requests

#establishes an endpoint for it the be used by the post method of the "requests" module. now containing my recently created username. alongside with all that, the token is now saved to a variable in order to be sent in the header of the request, a more secure method of interacting with APIs.

endpoint = "https://pixe.la/v1/users/mauboro/graphs"
TOKEN = "lkjdfhaoiuhhrf9183475y134iuh31oifjbqer8fu"

#creates the parameters needed to populate the HTTP post request with the required options for the graph creation.
graph_params = {
    "token": TOKEN, 
    "username": "mauboro",
    "id": "katamaster",
    "name": "katamaster",
    "type": "int",
    "unit": "commit",
    "color": "momiji"
}

#creates a dict(just like the graph_params dict) to store required info for the header of request.
headers = {
    "X-USER-TOKEN": TOKEN
}

#creates a variable to contain the request and its subsequent values in various formats, in that case, json. there are lots of ways to interact with "response" variables, unfortunately, I do not know most of them.
response = requests.post(url=endpoint, headers=headers, json=graph_params)
print(response.json())
