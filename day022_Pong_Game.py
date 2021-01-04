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

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# 將動畫關閉，直到呼叫 update()，搭配 update() 使用
screen.tracer(0)

# Create and move a paddle
paddle = Turtle()
paddle.shape("square")
# stretch_wid 及 stretch_len 為 20 的倍數
# stretch_wid (height 高度) 為 100 則給 5
# stretch_len (width 寬度) 為 20 則給 1
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    # 等 paddle 移至定位時再顯示，不然會看到 paddle 從中間移到旁邊
    # 要同時設置 screen.tracer(0)
    # 要放在 while 迴圈中不斷 update，不然按上下鍵時，畫面都不會更新
    screen.update()


screen.exitonclick()
