endpoint="http://localhost:8000/udr/2/"

import requests
response=requests.delete(endpoint)
print(response.json())