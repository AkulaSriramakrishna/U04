import json

#json_data is python object
json_data = {
    "name": "akhil",
    "password": "Test@123",
    "address": {
    "street": "mi road",
    "city": "Jaipur",
    "state": "Rajasthan"
}
}

print(type(json_data))
#data contains json values converted from json object
data =json.dumps(json_data)
print(type(data))
print(data)

#sending json value to file
with open("user.json",'w') as outfile:
    json.dump(data,outfile)

json_data1 = '{ "user": "root", "password": "rps@123" }'
data =json.dumps(json_data1)
with open("abc.json",'w') as outfile:
    json.dump(data,outfile)