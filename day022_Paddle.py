from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # shape 預設寬高為 20
        # stretch_wid 及 stretch_len 為 20 的倍數
        # stretch_wid (height 高度) 為 100 則給 5
        # stretch_len (width 寬度) 為 20 則給 1
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
