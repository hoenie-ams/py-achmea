import csv

# sales = 3061
# costs = 1778
sales = 0
costs = 0

with open("exercises/sales.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        sales = sales + float(row[2])
print(sales)

sales = 0

with open("exercises/sales.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sales = sales + float(row["Sales"])

print(sales)
