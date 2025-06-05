import requests
endpoint="http://localhost:8000/"
response=requests.get(endpoint,json={"query":"Hello World"})
print(response.json())

