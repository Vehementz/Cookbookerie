import requests
import json
results = requests.get("http://172.18.0.2/users")
data = json.loads(results.content)
print(type(data))
print(len(data))