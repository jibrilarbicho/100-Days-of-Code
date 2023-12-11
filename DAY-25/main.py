# import csv


# with open("/home/jibril/Documents/Python/DAY-25/weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
# print(tempratures)

# # print(data)
import pandas

data = pandas.read_csv("/home/jibril/Documents/Python/DAY-25/weather-data.csv")
print(data)
