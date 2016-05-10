#scoreboard.py

class Scoreboard():
	def __init__(self):
		self.result = 0
		self.penalties = 0
		self.handicap_points = 0
		self.timeouts = 5
		self.substituitions = 10
	def add_point(self, num_points=1):
		self.result += num_points

	def subtract_point(self, num_points=1):
		self.result -= num_points
	def print_score(self):
		print self.result

	def get_score(self):
		return self.result
