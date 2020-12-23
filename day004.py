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