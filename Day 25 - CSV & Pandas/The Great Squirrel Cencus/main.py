import pandas as pd

# TODO Create a separate CSV file that displays the count of squirrels by colour
# TODO Filter dataframe for colour
# TODO Count number of each colour in data frame
# TODO Create separate csv file containing colour data

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(df.info())
color = df["Primary Fur Color"]
# color.unique().to_list()
df.groupby(df["Primary Fur Color"])
print(df)