endpoint="http://localhost:8000/product/3/"
import requests

data_recived=requests.get(endpoint)
print(data_recived.json())