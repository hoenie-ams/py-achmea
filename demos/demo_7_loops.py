"""
Demo loops
"""

groceries = ["spam", "spam", "ham", "eggs"]

# D.R.Y.  Don't repeat yourself
print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[3])

i = 0
while i < 4:
    print(groceries[i])
    i = i + 1

for x in range(0, 4):
    print(groceries[x])

for item in groceries:
    print(item)

for x in range(0, 4):
    print(x + 1, groceries[x])

for x in enumerate(groceries):
    print(x[0] + 1, x[1])

for rank, item in enumerate(groceries, start=1):
    print(rank, item)

for item in groceries:
    if item == "ham":
        continue
    print(item)


for char in "Guido":
    print(char)

grades = {"A": 100, "B": 90}

for key in grades:
    print(key)

number = input("give me a number: ")
