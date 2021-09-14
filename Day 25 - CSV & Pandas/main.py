# with open("weather_data.csv") as wx_data:
#     days = wx_data.readlines()
#     data = [line.strip() for line in days]
#
# print(data)

import csv
temperatures = []
with open("weather_data.csv") as wx_data:
    data = csv.reader(wx_data)
    for row in data:
        print(row)
        temperatures.append(row[1])
temperatures = temperatures[1:]
for i in range(0, len(temperatures)-1):
    temperatures[i] = int(temperatures[i])

print(temperatures)

