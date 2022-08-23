import requests
import json
# address = "http://127.0.0.1:5000/"
#
# response = requests.get(address)

lst = [1, 2, 3, 4, 5]

d = {'list': lst}
address2 = "http://127.0.0.1:5000/something"

response2 = requests.post(address2, json=d)
returned_object=json.loads(response2.text)
print(type(returned_object))
print(returned_object)
