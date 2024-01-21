import csv

with open("weather_data.csv") as data:
    datas = csv.reader(data)
    temperatures = []
    for row in datas:
        if row[1] != "temp":
            temperatures.append(int(row[1]))


import pandas

print(pandas.read_csv("weather_data.csv"))
data = pandas.read_csv("weather_data.csv")

print("----------------------------------------")

print(data[data.temp == data.temp.min()])