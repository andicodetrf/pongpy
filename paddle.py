from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, pos):
		super().__init__()
		self.shape('square')
		self.penup()
		self.shapesize(stretch_wid=5, stretch_len=1)
		self.goto(pos)
		self.y_pos = 0

	def up(self):
		if self.ycor() < 230:
			new_y = self.ycor() + 30
			self.goto(self.xcor(), new_y)

	def down(self):
		if self.ycor() > -230:
			new_y = self.ycor() - 30
			self.goto(self.xcor(), new_y)