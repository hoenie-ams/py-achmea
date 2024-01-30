"""
Demo tuples
"""

flag = ("red", "white", "blue")

# tuple unpacking
first_color, second_color, third_color = flag

print(first_color)

a = (4, 5, 6)
print(type(a))
print(a[0:2])


fruits = ["apple", "banana", "orange"]
dairy = ["milk", "yoghurt"]
meats = ["ham", "sausage", "steak"]
vegetables = ["cucumber", "lettuce", "tomato"]

menu = (fruits, dairy, meats)
# menu[-1] = vegetables
meats[0] = "fish"
print(menu)
