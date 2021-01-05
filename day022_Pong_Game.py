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
from turtle import Screen
from day022_Paddle import Paddle
from day022_Ball import Ball
from day022_Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
# 將動畫關閉，直到呼叫 update()，搭配 update() 使用
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball and make it move
ball = Ball()

# Keep score
scoreboard = Scoreboard()

screen.listen()
# 用 onkeypress 可以按著按鍵就可以持續作用，而不用一直點擊按鍵
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # 讓速度慢一點

    # 等 paddle 移至定位時再顯示，不然會看到 paddle 從中間移到旁邊
    # 要同時設置 screen.tracer(0)
    # 要放在 while 迴圈中不斷 update，不然按上下鍵時，畫面都不會更新
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
