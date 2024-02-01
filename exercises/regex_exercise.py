import re

with open("exercises/ossec.log") as f:
    lines = f.readlines()


# print time for each line
for line in lines:
    result = re.search(r"(\d{2}:\d{2}:\d{2})", line)
    # print(result.group(1))

# count number of tcp connections
tcp_count = 0
for line in lines:
    result = re.search(r"TCP", line)
    if result:
        tcp_count += 1
print(f"TCP connections: {tcp_count}")

# print first ip address for each line
for line in lines:
    result = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
    if result:
        print(result.group(1))
