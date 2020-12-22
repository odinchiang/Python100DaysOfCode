# Data Types

# String
print("Hello"[1])
print("123" + "345")
print(type("Hello"))

# Integer
print(123 + 345)
print(123_345_789)
print(type(123))

# Float
print(3.1415926)
print(type(3.14))

# Boolean
print(True)
print(type(False))

# 類型轉換為字串 str()
lengthName = len(input("What is your name? "))
print("lengthName type: " + str(type(lengthName))) # <class 'int'>
lengthNameStr = str(lengthName)
print("lengthNameStr type: " + str(type(lengthNameStr))) # <class 'str'>
print("Your name has " + lengthNameStr + " characters.")

# 其他轉換 float(), int()
num = 123
print(type(num)) # <class 'int'>
print(type(float(num))) # <class 'float'>

# Example
print("===Example===")
chars = input("Type a two digit number: ")
sum = int(chars[0]) + int(chars[1])
print(sum)

# 運算
print(6 / 3) # 2.0 => float
print(2 ** 3) # 次方

# PEMDAS：
# Parentheses（括號）()
# Exponents（指數）**
# Multiplication（乘法）*
# Division（除法）/
# Addition（加法）+
# Subtraction（減法）-
print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0

# BMI Example
height = input("Please enter your height in m: ")
weight = input("Please enter your weight in kg: ")
bmi = float(weight) / ((float(height) ** 2))
print("Your BMI: " + str(int(bmi)))

# 四捨五入
print(round(8 / 3)) # 3
print(round(8 / 3, 2)) # 2.67

# 取餘數
print(8 // 3) # 2, 類型為 int

# f-String (字串插值, 用法類似 C# 的 $"")
score = 0
isWinning = True
print(f"Your score is {score}.")
print(f"Your height is {height} m.")
print(f"You are winning is {isWinning}")

# Example (離 90 歲還有多少時間)
age = input("What is your current age? ")
intForAgeLeft = 90 - int(age)
days = 365 * intForAgeLeft
weeks = 52 * intForAgeLeft
months = 12 * intForAgeLeft
print(f"You have {days} days, {weeks} weeks, and {months} months left.")