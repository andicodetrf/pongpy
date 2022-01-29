from turtle import Turtle, Screen


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.ht()
		self.penup()
		self.l_score = 0
		self.r_score = 0
		self.update_score()

	def update_score(self):
		self.clear()
		self.goto(-300, 270)
		self.write("'e' = up, \n's' = down", align="center", font=("Courier", 10, "normal"))
		self.goto(300, 270)
		self.write("up-arrow = up, \ndown-arrow = down", align="center", font=("Courier", 10, "normal"))
		self.goto(-100, 250)
		self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
		self.goto(100, 250)
		self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

	def l_point(self):
		self.l_score += 1
		self.update_score()

	def r_point(self):
		self.r_score += 1
		self.update_score()