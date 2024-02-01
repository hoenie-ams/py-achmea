import pandas as pd

cars = pd.read_csv("https://opendata.rdw.nl/resource/m9d7-ebf2.csv")

# print(cars.head())


dfs = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

print(dfs[0])
