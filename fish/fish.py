# Fish

import random

class Fish(object):

	def __init__(self, name):
		print 'a new fish'
		self.name = name
		self.x = 0
		self.y = 0


	def say_name(self):
		print 'my name is: ' + self.name + ', Im at x: ' + str(self.x) + ', y: ' + str(self.y)

	def move_right(self):
		self.x += 10

	def move_left(self):
		self.x -= 10

	def move_up(self):
		self.y += 10

	def move_down(self):
		self.y -= 10

	def move_random(self):
		r = random.randint(-10, 10)
		self.x += r
		r = random.randint(-10, 10)
		self.y += r

