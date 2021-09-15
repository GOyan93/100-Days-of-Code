# with open("weather_data.csv") as wx_data:
#     days = wx_data.readlines()
#     data = [line.strip() for line in days]
#
# print(data)

# import csv
# import pandas
#
# temperatures = []
# with open("weather_data.csv") as wx_data:
#     data = csv.reader(wx_data)
#     for row in data:
#         print(row)
#         temperatures.append(row[1])
# temperatures = temperatures[1:]
# for i in range(0, len(temperatures)-1):
#     temperatures[i] = int(temperatures[i])
#
# print(temperatures)
import pandas
import numpy

df = pandas.read_csv("weather_data.csv")
# temp_data = df['temp']
# max_temp = temp_data.max()
# print(df[df.temp == max_temp])

Monday = df[df.day == "Monday"]
monday_temp_c = Monday["temp"]

def temp_convert(temperature):
    return (9 / 5) * temperature + 32

print(temp_convert(monday_temp_c))
