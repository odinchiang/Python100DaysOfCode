# Intermediate - Working with CSV Data and the Pandas Library

# CSV: Comma Separated Values

# 傳統方式處理 csv 檔案
with open("weather_data.csv") as file:
    files = file.readlines()
    """
    ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n',
    'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']
    """
    # 需自行處理 \n 的問題

# 使用 csv 模組處理 csv 檔案
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    """
    ['day', 'temp', 'condition']
    ['Monday', '12', 'Sunny']
    ['Tuesday', '14', 'Rain']
    ['Wednesday', '15', 'Rain']
    ['Thursday', '14', 'Cloudy']
    ['Friday', '21', 'Sunny']
    ['Saturday', '22', 'Sunny']
    ['Sunday', '24', 'Sunny']
    """

# 使用 pandas 模組處理 csv 檔案
import pandas

csv_data = pandas.read_csv("weather_data.csv")
# print(csv_data)
"""
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
"""
# print(csv_data["temp"])
"""
0    12
1    14
2    15
3    14
4    21
5    22
6    24
"""

print(type(csv_data))  # <class 'pandas.core.frame.DataFrame'>
"""
pandas 模組有兩種資料結構：
1. Series (一維)：類似 list，表格的每一欄位資料即為 Series
2. DataFrame (二維)：即表格
"""

# 轉換為 dictionary
data_dict = csv_data.to_dict()
print(data_dict)
"""
{
    'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 
    'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 
    'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
}
"""

print(type(csv_data["temp"]))  # <class 'pandas.core.series.Series'>
temp_list = csv_data["temp"].to_list()

# 轉換為 list 計算平均值
print(temp_list)  # [12, 14, 15, 14, 21, 22, 24]
average_temp = sum(temp_list) / len(temp_list)
print(average_temp)  # 17.428571428571427

# 直接使用 pandas 模組計算平均值
print(csv_data["temp"].mean())  # 17.428571428571427

# 最大值
print(csv_data["temp"].max())  # 24

# 最小值
print(csv_data["temp"].min())  # 12

# Get Data in Columns
print(csv_data["condition"])
print(csv_data.condition)

# Get Data in Row
print(csv_data[csv_data.day == "Monday"])
"""
      day  temp condition
0  Monday    12     Sunny
"""

# 取得溫度最高的那一列資料
temp_max_row = csv_data[csv_data.temp == csv_data.temp.max()]
print(temp_max_row)
"""
      day  temp condition
6  Sunday    24     Sunny
"""

monday = csv_data[csv_data.day == "Monday"]
print(monday.condition)
# 0    Sunny
print(monday.temp * 9 / 5 + 32)  # 取得 Monday 那一列的攝氏溫度並轉為華氏溫度
# 0    53.6

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_frame = pandas.DataFrame(data_dict)
print(data_frame)
"""
  students  scores
0      Amy      76
1    James      56
2   Angela      65
"""

# 將 DataFrame 轉為 csv 檔案
data_frame.to_csv("new_data.csv", index=False)

print("====================================================================")

# Example - The Great Squirrel Census Data Analysis
# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

# squirrel_count.csv
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv", index=False)
