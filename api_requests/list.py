endpoint="http://localhost:8000/"

import requests
resopnse=requests.get(endpoint)
print(resopnse.json())
