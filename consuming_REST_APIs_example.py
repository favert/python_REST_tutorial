# this code is based on tutorial for using python and REST API under
# https://realpython.com/api-integration-in-python/

import requests

# some test for retrieving all entries response from REST API
api_url = "http://jsonplaceholder.typicode.com/todos"
response = requests.get(api_url)
print(f'(GET) Jason: {response.json()}')
print(f'(GET) Code: {response.status_code}')

# some test for retrieving all entries response from REST API
api_url = "http://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(f'(GET one) Jason: {response.json()}')
print(f'(GET one) Code: {response.status_code}')

# some test for POST data on REST API
api_url = "http://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
print(f'(POST) Jason: {response.json()}')
print(f'(POST) Code: {response.status_code}')

# some test for POST data on REST API without setting json attribute 
# on request
import json
api_url = "http://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
print(f'(POST Content-type) Jason: {response.json()}')
print(f'(POST Content-type) Code: {response.status_code}')

# some test for PATCH (change specific info) data on REST API
api_url = "http://jsonplaceholder.typicode.com/todos/10"
response = requests.get(api_url)
print(f'(PATCH) {response.json()}')
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
print(f'(PATCH) Jason: {response.json()}')
print(f'(PATCH) Code: {response.status_code}')

# some test for DELETE data on REST API
api_url = "http://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(f'(DELETE) Jason: {response.json()}')
print(f'(DELETE) Code: {response.status_code}')
