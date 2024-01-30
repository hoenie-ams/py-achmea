"""
Demo of dictionaries (HashMap/HashTable)
"""

person = {"name": "John Doe",
          "age": 42,
          "email": "john@doe.com"}

print(type(person))
print(person)

print(person["name"])
print(person.get("name", "John"))
