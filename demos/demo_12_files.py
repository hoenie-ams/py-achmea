

f = open("demos/zen.txt")

text = f.read()

f.close()

with open("demos/zen.txt", "r") as file:
    # text = file.read().rstrip()
    # lines = file.read().splitlines()
    lines = file.readlines()
    new = []
    for line in lines:
        new.append(line.rstrip())

print(new)
