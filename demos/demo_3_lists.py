"""
Demo working with lists
"""

my_list = []

print(type(my_list))

groceries = ["spam", "spam", "ham", "eggs"]

print(groceries[0])
print(groceries[0:2])

print(groceries.append("cheese"))
print(groceries)

demo_list = [0, 1, 2, ["a", "b"]]
print(demo_list)

chars = demo_list[-1]
print(chars[0])

print(demo_list[3][0])


grocery_list = ['spam', 'ham', 'eggs', 'cheese']

# 1
grocery_list[-1] = 'onion'

# 2
grocery_list.pop()
grocery_list.append('onion')

# 3
grocery_list.remove('cheese')
grocery_list.append('onion')

# 4
del grocery_list[3]
grocery_list.append('onion')
