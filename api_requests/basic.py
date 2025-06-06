import requests
endpoint="http://localhost:8000/"
response=requests.get(endpoint,params={"pk":100},json={"query":"Hello World"})
print(response.json())

