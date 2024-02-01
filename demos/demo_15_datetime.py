"""
Demo of datetime
"""

from datetime import datetime, date

today = datetime(2024, 2, 1, 9, 15)
print(today)

start_of_year = date(2024, 1, 1)
print(start_of_year)

print(today - start_of_year)

example_1 = "31/12/2024"
datetime.strptime(example_1, "%d/%m/%Y")

example_2 = "12-31-2019"
datetime.strptime(example_2, "%m-%d-%Y")
