import requests

#establishes an endpoint for it the be used by the post method of the "requests" module.
endpoint = "https://pixe.la/v1/users"

#creates the parameters needed to populate the HTTP post request.
params = {
    "token": "lkjdfhaoiuhhrf9183475y134iuh31oifjbqer8fu",
    "username": "mauboro",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
 
#creates a variable to contain the request and its subsequent values in various formats, in that case, json. there are lots of ways to interact with "response" variables, unfortunately, I do not know most of them.
response = requests.post(url=endpoint, json=params)
print(response.json())
