from requests import get
print(type(get))
target = "http://172.18.0.2"
response = get(target)
print(response)


