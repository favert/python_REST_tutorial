import requests

api_url = "http://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(f'{response.json()}')
