import csv

with open("devices.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "IP"])
    for x in range(10):
        writer.writerow([f"Device {x}", f"192.168.0.{x}"])


with open("devices.csv", "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        print(row[0], row[1])


with open("names.csv", "w") as csvfile:
    columns = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=columns)

    writer.writeheader()
    writer.writerow({"first_name": "John", "last_name": "Doe"})
    writer.writerow({"first_name": "Jane", "last_name": "Doe"})
    writer.writerow({"first_name": "Suzy", "last_name": "Doe"})


with open("names.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
