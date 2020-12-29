# Beginner - Scope & Number Guessing Game

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # 2

increase_enemies()
print(f"enemies outside function: {enemies}") # 1

# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    
drink_potion() # 2
# print(potion_strength) # Error

# Global Scope
player_health = 10 # Global variable

def drink_potion2():
    potion_strength = 2 # Local variable
    print(player_health) # 10

drink_potion2()
print(player_health)

# Namespace
def game():
    def drink_potion3():
        potion_strength = 3
        print(player_health)
    drink_potion3()

# drink_potion3() # Error

# There is no Block Scope in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

# 雖然 new_enemy 是在 if 中宣告，if 外仍可以存取
print(new_enemy)

# 只有函式有 Local Scope，其他像是 if、for、while 等並沒有 Local Scope 範圍

# Modifying Global Scope (在函式中修改全域變數)
name = "Mark"

def change_name():
    # 用 global 關鍵字在函式中定義一個跟全域變數一樣名稱的變數
    # 不建議此種用法
    # 不要在函式中修改全域變數
    global name
    name += "Mary"
    print(f"name inside function: {name}") # MarkMary

# 建議用函式 return 的方式
def change_name2():
    print(f"name inside function: {name}")
    return name + "Mary"

change_name()
print(f"name outside function: {name}") # MarkMary
print(change_name2())

# Global Constants
# 用全部大寫表示常數
PI = 3.1415926
URL = "https://www.google.com.tw"
TWITTER_HANDLE = "@yu_angela"


print("===========================================================")


# Example - Number Guessing Game
from os import system
from random import randint

system("cls")

def get_attempts(level):
    """
    根據 level 回傳可猜次數
    """
    if level == "hard":
        return 5
    elif level == "easy":
        return 10
    else:
        return 0

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level != "easy" and level != "hard":
        print("Wrong Type!")
        return
    
    attempts = get_attempts(level)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        
        if answer == guess_number:
            print(f"You got it! The answer was {answer}.")
            break
        elif answer > guess_number:
            print(f"Too low.")
        elif answer < guess_number:
            print(f"Too high.")
            
        attempts -= 1
        if attempts > 0:
            print("Guess again.")
        
        
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        
play_game()