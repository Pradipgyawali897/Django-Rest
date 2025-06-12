import requests
endpoint="http://localhost:8000/"
response=requests.post(endpoint,params={"id":1},json={"title":"ram",
                                                     "price":100
                                                     })
print(response.json())

