# Beginner - Python Loops

import random

# 檢查 email 個資是否已被駭客竊取
# https://haveibeenpwned.com/

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(f"{fruit} Pie")

print("==========================")
    
# Example - Average Height
# 不能用 sum() 及 len()
heightString = input("Input a list of student heights in cm (eg: 156 178 165 171 187): ")
heightList = heightString.split() # 針對空格拆分，不需要加參數

totalHeight = 0 # 身高總和
countHeight = 0 # 身高個數
for height in heightList:
    totalHeight += int(height)
    countHeight += 1

averageHeight = totalHeight / countHeight # 身高平均值
print(round(averageHeight))

# 利用內建方法

for n in range(0, len(heightList)):
    heightList[n] = int(heightList[n])

totalHeight = sum(heightList)
averageHeight = totalHeight / len(heightList)
print(round(averageHeight))

print("==========================")

# Example - Highest Score
# 不能用 max()
scoreString = input("Input a list of student scores: (eg: 78 65 89 86 55 91 64 89)\n")
scoreList = scoreString.split()
maxScore = 0

for score in scoreList:
    if maxScore < int(score):
        maxScore = int(score)

print(f"The highest score in the class is: {maxScore}")

# 利用內建方法
for n in range(0, len(scoreList)):
    scoreList[n] = int(scoreList[n])

maxScore = max(scoreList)

print(f"The highest score in the class is: {maxScore}")

print("==========================")

# For loop with Range
# range(start, stop[, step])
# 範圍為 start ~ stop - step
for number in range(1, 10):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total) # 5050

print("==========================")

# Example - Adding Evens
'''
You are going to write a program that calculates the sum of all
the even numbers from 1 to 100, including 2 and 100.

e.g. 2 + 4 + 6 + 8 +10 ... + 98 + 100

Important, there should only be 1 print statement in your console
output. It should just print the final total and not every step of the calculation.
'''
evenTotal = 0
for number in range(2, 102, 2):
    evenTotal += number
print(evenTotal) # 2550

evenTotal = 0
for number in range(1, 101):
    if number % 2 == 0:
        evenTotal += number
print(evenTotal) # 2550

print("==========================")

# Example - FizzBuzz
'''
You are going to write a program that automatically prints the
solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

1. When the number is divisible by 3 then instead of printing the
   number it should print "Fizz".
2. When the number is divisible by 5, then instead of printing
   the number it should print "Buzz".
3. When the number is divisible by both 3 and 5 e.g. 15 then
   instead of the number it should print "FizzBuzz"
'''
for number in range(1, 101):
    isBy3 = number % 3 == 0
    isBy5 = number % 5 == 0
    if isBy3 and isBy5:
        print("FizzBuzz")
    elif isBy3:
        print("Fizz")
    elif isBy5:
        print("Buzz")
    else:
        print(number)

print("==========================")

# Example - Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwordCount = nr_letters + nr_numbers + nr_symbols

letterCount = len(letters) # 52
symbolCount = len(symbols) # 9
numberCount = len(numbers) # 10

# Eazy Level (密碼 = letter 字串 + symbol 字串 + number 字串)

passwordNoRandom = []
for i in range(0, nr_letters):
    # passwordNoRandom.append(letters[random.randint(0, letterCount - 1)])
    passwordNoRandom.append(random.choice(letters))

for i in range(0, nr_symbols):
    # passwordNoRandom.append(symbols[random.randint(0, symbolCount - 1 )])
    passwordNoRandom.append(random.choice(symbols))

for i in range(0, nr_numbers):
    # passwordNoRandom.append(numbers[random.randint(0, numberCount - 1)])
    passwordNoRandom.append(random.choice(numbers))

eazyPassword = "".join(passwordNoRandom)
print(f"Eazy Level Password: {eazyPassword}")

# Hard Level (將 Eazy Level 的密碼的字元打亂)

# 用 for 迴圈，每次亂數取得 Eazy Level 密碼的字元，取完之後將該字元刪除，重複直到取完為止
# password = ""
# for i in range(0, passwordCount):
#     count = len(passwordNoRandom)
#     index = random.randint(0, count - 1)
#     password += passwordNoRandom[index]
#     del(passwordNoRandom[index])

# 直接用 random.shuffle(集合) 將集合中的元素打亂
random.shuffle(passwordNoRandom)
password = "".join(passwordNoRandom)

print(f"Hard Level Password: {password}")




