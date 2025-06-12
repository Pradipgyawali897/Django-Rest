endpoint="http://localhost:8000/"
import requests
data={
    'title':"Hello",
    'content':"ham",
    "price":12,
}
data_recived=requests.post(endpoint,json=data)
print(data_recived.json())