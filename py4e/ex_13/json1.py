import json
data = '''{
    "name" : "chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

#info 는 dictionary
info = json.loads(data)
print('Name',info["name"])
print("Phone", info['phone']['type'])
print('Hide',info["email"]["hide"])
