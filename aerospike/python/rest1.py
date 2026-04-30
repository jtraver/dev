
import requests
import json

url = "http://localhost:8080/v1/kvs/test/demo/hello-key"
payload = {"bins": {"greeting": "Hello from REST!"}}

# Write a record
response = requests.post(url, json=payload)
print(f"Write Status: {response.status_code}")

# Read a record back
response = requests.get(url)
print(f"Read Record: {response.json()['bins']['greeting']}")

