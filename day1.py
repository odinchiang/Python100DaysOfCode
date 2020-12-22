# 輸出
print("Hello world")
print("print('what to print')")
print("print(\"what to print\")")
print('print("what to print")')

print("=============")

# 換列
print("Hello world!\nHello world!\nHello world!")

# 錯誤訊息

# SyntaxError: EOL while scanning string literal
# 語法錯誤，少寫引號或括號等

# IndentationError: unexpected indent
# 出現沒有必要的縮排

# 輸入
name = input("What is your name? ")
print(name)
print(len(name))

name = 123
print(name)

print("===案例練習===")
print("Welcome to the Band Name Generator.")
city = input("What's name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + petName)

