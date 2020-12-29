# Beginner - Debugging: How to Find and Fix Errors in your Code

# 1. Describe Problem
# 2. Reproduce the Bug
# 3. Play Computer
# 4. Fix the Errors
# 5. Print is Your Friend
# 6. Use a Debugger
# 7. Take a Break
# 8. Ask a Friend
# 9. Run Your Code Often
# 10. Ask StackOverflow

############DEBUGGING#####################

# # Describe Problem
# 執行之後沒有文字出現
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# 多執行幾次會出錯
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# 若為 1994 或 小於等於 1980 會沒有任何文字出現
# year = int(input("What's your year of birth? "))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])


# 解答

# 1. Describe Problem
# range 函式的第二個參數數字不包含在內
# range 的第二個參數改為 21
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

print("==========================")

# 2. Reproduce the Bug
# 多執行幾次會出錯，原因為 randint 第二個數字超出 list 的最大索引值
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, len(dice_imgs) - 1)
print(dice_imgs[dice_num])

print("==========================")

# 3. Play Computer
year = int(input("What's your year of birth? "))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
else:
    print("You are older.")

print("==========================")

# 4. Fix the Errors
age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")

print("==========================")

# 5. Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)

print("==========================")

# 6. Use a Debugger
# http://www.pythontutor.com/visualize.html#mode=edit
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])


