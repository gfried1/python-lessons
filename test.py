class Scoreboard():
	def __init__(self):
		self.result = 0
		self.penalties = 0
		self.handicap_points = 0
		self.timeouts = 5
		self.substituitions = 10


	def add_point(self, num_points=1):
		self.result += num_points

	def print_score(self):
		print self.result



my_score = Scoreboard()

your_score = Scoreboard()

my_score.add_point(5)

my_score.add_point()

your_score.add_point()


print 'my score is:'
my_score.print_score()

print 'your score is:'
your_score.print_score()
