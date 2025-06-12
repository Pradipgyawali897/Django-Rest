import requests

endpoint = "http://localhost:8000/udr/1/"
data = {
    'title': "man",
    'content': "man",
    'price': 12,
}

try:
    response = requests.put(endpoint, json=data)  # Add headers if needed: headers={"Authorization": "Bearer your_token"}
    response.raise_for_status()  # Raises an error for 4xx/5xx status codes

    if response.status_code in (200, 201):
        print("Success:", response.json() if response.content else "No content returned")
    else:
        print(f"Unexpected status code: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the server. Ensure it’s running on localhost:8000")
except requests.exceptions.JSONDecodeError:
    print("Error: Response is not valid JSON. Raw response:", response.text)
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e} (Status code: {response.status_code})")
except Exception as e:
    print(f"Unexpected error: {e}")