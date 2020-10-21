import json
user = {
    "id" : "dekis",
    "password" : "1234",
    "age" : 30,
    "hobby" : ["football","programming"]
}

#파이선 변수를 JSON객체로 변환
json_data = json.dumps(user, indent=4)
print(json_data)