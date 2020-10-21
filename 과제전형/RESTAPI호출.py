import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

data = response.json()
print(data)
name_list = []
username_list = []
for user in data:
    name_list.append(user['name'])
    username_list.append(user['email'])


print(name_list)
print(username_list)