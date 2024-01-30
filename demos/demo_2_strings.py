"""
Strings - working with text
"""

greeting = 'hello "beautiful" world'

print(greeting)

print(greeting[0])
print(greeting[0:5])
print(greeting.split())

print(1, 2, sep=",", end=" ")
print(3)


name = "Joris"
city = "Zeist"

print("Hello my name is %s and I live in %s." % (name, city))
print("Hello my name is " + name + " and I live in " + city + ".")
print("Hello my name is {} and I live in {}.".format(name, city))
print(f"Hello my name is {name} and I live in {city}.")
