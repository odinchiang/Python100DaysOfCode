# Beginner - Randomisation and Python Lists

import random # 匯入 python 的 random 模組
import my_module # 匯入自定義的模組

# Random Module
# 梅森旋轉演算法（Mersenne twister）
# https://en.wikipedia.org/wiki/Mersenne_Twister
# https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

print(random.randint(100, 200)) # 產生 100 ~ 200 的隨機整數 (包含頭尾的數字)

print(random.random()) # 產生 0 ~ 1 的浮點數隨機數 (0 ~ 0.999999...，不包含 1)
print(random.random() * 5) # 產生 0 ~ 5 的浮點隨機數 (0 ~ 4.99999...)

# Example - Heads or Tails
randomSide = random.randint(0, 1)
if randomSide == 1:
    print("Heads")
else:
    print("Tails")

print("=============")

# List

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# List 方法：https://docs.python.org/3/tutorial/datastructures.html
states_of_america = ["Delaware", "Pennsylvania", "Georgia"]
print(states_of_america)
print(states_of_america[1])
states_of_america[1] = "Pencilvania"
print(states_of_america[1])
states_of_america.append("New Jersey") # 增加一個元素
print(states_of_america)
states_of_america.extend(["Virginia", "New York"]) # 用集合的方式增加
print(states_of_america)

# Example - Who's Paying
'''
You are going to write a program which will select a
random name from a list of names. The person selected
will have to pay for everybody's food bill.
'''
# Convert String to List in Python
# https://www.askpython.com/python/string/convert-string-to-list-in-python
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") # 字串轉換為集合

namescount = len(names) # 集合裡元素的數量
selectedIndex = random.randint(0, namescount - 1) # 取得集合索引數的亂數
selectedName = names[selectedIndex] # 取得該亂數索引的元素

selectedName = random.choice(names) # 直接使用 random.choice(集合) 隨機取得元素
print(f"{selectedName} is going to buy the meal today!")

print("=============")

# Nested List
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]
print(dirty_dozen)
fruits = ["Strawberries", "Nectarines"]
vegetables = ["Spinach", "Kale", "Tomatoes"]
# 此寫法產生巢狀集合，集合中有兩個集合，類似二維陣列
nested_dirty_dozen = [fruits, vegetables]
print(nested_dirty_dozen)
print(nested_dirty_dozen[1][1]) # Kale

print("=============")

# Example - Treasure Map
# 輸入第幾列第幾欄，將該位置上的方框改為 X
# emoji：表情符號
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if len(position) == 2 and position.isnumeric():
    row = int(position[0])
    column = int(position[1])
    map[row-1][column-1] = "X"
    print(f"{row1}\n{row2}\n{row3}")
else:
    print("Please enter 2 numbers!")

print("=============")

# Example - 剪刀(scissors)石頭(rock)布(paper)遊戲
# https://www.wrpsa.com/
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
myChoise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if myChoise > 2 or myChoise < 0:
    print("You typed an invalid number, You Lose!")
else:
    computerChoise = random.randint(0, 2)
    print(list[myChoise])
    print("Computer chose:")
    print(list[computerChoise])
    
    if myChoise == computerChoise:
        print("It's a draw!")
    elif myChoise == 0 and computerChoise == 2:
        print("You Win!")
    elif myChoise == 2 and computerChoise == 0:
        print("You Lose!")
    elif myChoise > computerChoise:
        print("You Win!")
    else:
        print("You Lose!")

