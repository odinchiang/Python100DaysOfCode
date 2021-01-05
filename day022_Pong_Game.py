# Intermediate - Build Pong: The Famous Arcade Game

# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score

# Create the screen
from turtle import Screen, Turtle
from day022_Paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# 將動畫關閉，直到呼叫 update()，搭配 update() 使用
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    # 等 paddle 移至定位時再顯示，不然會看到 paddle 從中間移到旁邊
    # 要同時設置 screen.tracer(0)
    # 要放在 while 迴圈中不斷 update，不然按上下鍵時，畫面都不會更新
    screen.update()


screen.exitonclick()
