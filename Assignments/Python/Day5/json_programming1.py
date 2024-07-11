import json

json_data ='{ "user": "Akhil", "password": "Test@123" }'

python_json=json.loads(json_data)

for k in python_json:
    print(k)

#Reading json data from file

f = open('user.json')
data = json.load(f)
print(data)

x = json.loads(data)

#indenting the json data
y = json.dumps(x,indent=2)
print(y)


with open("user.json",'r') as f:
    data=json.load(f)

user=data["user"]
password=data["password"]

print(user)
print(password)