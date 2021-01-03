# Intermediate - Turtle & the Graphical User Interface (GUI)

from turtle import Turtle, Screen
import turtle as t  # t 為別名(alias)
import random

# turtle graph documentation
# https://docs.python.org/3/library/turtle.html

# Turtle Colors
# https://cs111.wellesley.edu/labs/lab01/colors

# Trinket Turtle Colors
# https://trinket.io/docs/colors

# 要用 rgb 設定 turtle.color 時，colormode 要設定為 255
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# turtle 畫筆
tim = Turtle()
# tim.shape("turtle")
tim.color("red")

##########################################################################

# Example - 繪製矩形
# for _ in range(4):
#     tim.forward(100)  # 前進
#     tim.right(90)  # 往右轉 90 度

# Example - 繪製 dashed line (將筆刷提起移動一小段，再放下畫一小段，達到繪製虛線的目的)
# tim.left(90)
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

##########################################################################

# Example - 利用迴圈繪製多邊形
# def draw_shape(num_sides):
#     """繪製 n 邊形"""
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(360 / num_sides)
#
#
# colors = ["green yellow", "firebrick", "orange", "blue", "orchid", "dark magenta"]
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

##########################################################################

# Example - Draw a Random Walk
# 隨機漫步(Random Walk)
# https://en.wikipedia.org/wiki/Random_walk
# https://www.w3schools.com/colors/colors_rgb.asp
# angles = [0, 90, 180, 270]
# tim.pensize(8)
# tim.speed("normal")

# while True:
#     tim.setheading(random.choice(angles))
#     tim.color(random_color())
#     tim.forward(20)

##########################################################################

# Example - Make a Spirograph
tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(10)

##########################################################################

# 開啟視窗
screen = t.Screen()
screen.exitonclick()
