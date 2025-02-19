import json
from interface_agent import IWriter
import requests
import uuid


class NetworkWriter(IWriter):

    def send_data(self, data: str, machine_name: str) -> None:
        # = {"data": data}
        response = requests.post(machine_name, json= data)
        if response.status_code == 200:
            print(response.json())

        print(response)
        print(type(response))





z = "    \n yeruham    !!!!!!!!!!!"
x = NetworkWriter()
x.send_data(z, "http://127.0.0.1:5000/n")

