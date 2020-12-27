# Beginner - Funciton Parameters & Caesar Cipher (凱撒密碼)

import math

# Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")
    
greet()

print("========================")

# Function that allows for input

# 定義的參數稱為 Parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

# 使用函式時實際代入的值稱為 Argument
greet_with_name("Odin")

print("========================")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}")
    
# Positional Arguments
# Arguments 按照 Parameters 的順序依次帶入
greet_with("Odin", "Taipei")

# Keyword Arguments
greet_with(location = "Taipei", name = "Odin")

print("========================")

# Example - Area Calc
'''
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height ✖️ wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 ✖️ 4) ÷ 5 = 1.6
But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
'''
def calc_can_number(width, height, coverage):
    # 無條件進位：math.ceil(float)
    can_number = math.ceil(width * height / coverage)
    print(f"You'll need {can_number} cans of paint.")
    
width = float(input("Width in meter? "))
height = float(input("Height in meter? "))
coverage = 5
calc_can_number(width, height, coverage)

print("========================")

# Example - Prime Number Checker
'''
You need to write a function that checks whether if the number passed into it is a prime number or not.
e.g. 2 is a prime number because it's only divisible by 1 and 2.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
'''
# https://en.wikipedia.org/wiki/Prime_number

def check_prime(number):
    if number == 1:
        print("1 is a prime number.")
    
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number")

n = int(input("Check this number: "))
check_prime(number = n)

print("========================")

# Example - Caesar Cipher (凱撒密碼)

from day008art import logo

# 加密
def encrypt(plain_text, shift_amount):
    encrypt_text = ""
    shift_amount = arrange_shift_amount(shift_amount, len(alphabet))
    # 遍歷每個字母
    for letter in plain_text:
        if letter in alphabet:
            # 取得該字母在 alphabet 集合中的索引值
            index = alphabet.index(letter)
            index += shift_amount
            # 超過最大索引值，則從頭開始取
            if index > (len(alphabet) - 1):
                index -= (len(alphabet))
            encrypt_text += alphabet[index]
        else:
            encrypt_text += letter
    print(f"Here's the encoded result: {encrypt_text}")

# 解密
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    shift_amount = arrange_shift_amount(shift_amount, len(alphabet))
    for letter in cipher_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            index -= shift_amount
            plain_text += alphabet[index]
        else:
            plain_text += letter
    print(f"Here's the decoded result: {plain_text}")
    
# 加密或解密
# start_text: text to encode or decode
# shift_amount: int
# cipher_direction: "encode" or "decode"
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    shift_amount = arrange_shift_amount(shift_amount, len(alphabet))
    # 若為解密，將 shift_amount 加上負號
    if cipher_direction == "decode":
        shift_amount *= -1
    # 遍歷每個字母
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            # 超過最大索引值且為加密，則從頭開始取
            if new_position > (len(alphabet) - 1) and shift_amount > 0:
                new_position -= (len(alphabet))
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"Here's the {cipher_direction}d result: {end_text}")

# 若位移數量超過 alphabet 的數量，則需要進行模數處理
def arrange_shift_amount(shift_amount, length):
    while shift_amount > length:
        shift_amount %= length
    return shift_amount

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

is_again = "yes"
while is_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != "encode" and direction != "decode":
        print("Please type 'encode' or decode!")
        is_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        continue;
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
        
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)

    is_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

print("Goodbye!")