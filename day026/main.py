# Intermediate - List Comprehension and the NATO Alphabet

import random
import pandas

# 可應用的範圍
# list, range, string, tuple

# === List Comprehension ===
# 語法：new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]  # [2, 3, 4]

name = "Odin"
letter_list = [letter for letter in name]  # ["O", "d", "i", "n"]

double_range = [n * 2 for n in range(1, 5)]  # [2, 4, 6, 8]

# Conditional List Comprehension
# 語法： new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]  # ["Alex", "Beth", "Dave"]
long_names = [name.upper() for name in names if len(name) > 5]  # ["CAROLINE", "ELEANOR", "FREDDIE"]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]  # [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]  # [2, 8, 34]

# 讀取 file1.txt 及 file2.txt 並比較兩者資料，取出相同的資料
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(n) for n in file_1_data if n in file_2_data]
# [3, 6, 5, 33, 12, 7, 42, 13]

# === Dictionary Comprehension ===
# 語法(list 轉 dictionary)：
# new_dict = {new_key: new_value for item in list}
# 語法(dictionary 轉 dictionary)：
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# 語法(有條件的 dictionary 轉 dictionary)：
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student: random.randint(0, 100) for student in names}
# {'Alex': 70, 'Beth': 19, 'Caroline': 92, 'Dave': 12, 'Eleanor': 47, 'Freddie': 59}
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
# {'Alex': 70, 'Caroline': 92}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list = sentence.split()
# ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']
result = {item: len(item) for item in sentence_list}
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
# {'Monday': 53.6, 'Tuesday': 57.2, 'Wednesday': 59.0, 'Thursday': 57.2,
# 'Friday': 69.8, 'Saturday': 71.6, 'Sunday': 75.2}

print("======================================================")
# Iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(f"key: {key}, value: {value}")

print("======================================================")

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

print("======================================================")

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)

print("======================================================")

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(f"name: {row.student}, score: {row.score}")
