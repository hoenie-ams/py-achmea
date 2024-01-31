import json

person = {
    'id': 12,
    'name': 'Jane',
    'is_active': True,
    'phone': None
}

with open('person.json', 'w') as json_file:
    json.dump(person, json_file, indent=4, sort_keys=True)


with open('person.json') as json_file:
    data = json.load(json_file)
    # print(data)


# print(json.dumps(person))


print(
    json.loads('{"id": 12, "name": "Jane", "is_active": true, "phone": null}'))
