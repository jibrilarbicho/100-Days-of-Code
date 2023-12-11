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

# data = pandas.read_csv("/home/jibril/Documents/Python/DAY-25/weather-data.csv")
# # data_dict = data.to_dict()  # change it to dictionary
# # print(data_dict)
# # temp_list = data[
# #     "temp"
# # ].tolist()  # it takes one column which that are bellow temp column
# # print(temp_list)
# # print(data["temp"].max())
# # print(data["temp"].min())
# # print(data["temp"].mean())

# # print(data[data.day == "Monday"])  # it treated as dictionary
# # print(data)
# # print(data["temp"].max())  # the same as the bellow
# # print(data.temp.max())
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# # Create a dataframe from scratch
# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}
# data = pandas.DataFrame(data_dict)
# print(data)
data = pandas.read_csv("/home/jibril/Documents/Python/DAY-25/Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)
dataDic = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count],
}
dataframe = pandas.DataFrame(dataDic)
dataCSV = dataframe.to_csv("squirrel_count.csv")
print(dataframe)
