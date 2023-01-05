import requests
from datetime import datetime

class GraphMaster:
    def __init__(self):
        self.token = "lkjdfhaoiuhhrf9183475y134iuh31oifjbqer8fu"
        self.date = datetime.now().strftime("%Y%m%d")
        self.header = {"X-USER-TOKEN": self.token}
        
    def insert_pixel_in_pomokiller(self, quantity):
        graph_params = {
            "token": self.token, 
            "unit": "commit",
            "date": self.date,
            "quantity": quantity 
        }
        endpoint = "https://pixe.la/v1/users/mauboro/graphs/pomokiller"
        response = requests.post(url=endpoint, headers=self.header, json=graph_params)
        print(response.json())

    def insert_pixel_in_katamaster(self, quantity):
        graph_params = {
            "token": self.token, 
            "unit": "commit",
            "date": self.date,
            "quantity": quantity 
        }
        endpoint = "https://pixe.la/v1/users/mauboro/graphs/katamaster"
        response = requests.post(url=endpoint, headers=self.header, json=graph_params)
        print(response.json())
