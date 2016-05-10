from spot import Spot

class Board(object):

	def __init__(self, difficulty):

		self.difficulty = difficulty

		# rows and columns are set to a number in set_up_spot_list()
		self.rows = None
		self.columns = None

		self.title = 'The Board'
		self.letter_list= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

		self.spot_list = []
		self.set_up_spot_list()

	def set_up_spot_list(self):

		# the size of the board depends on the difficulty
		if self.difficulty == 'easy':
			self.rows = 5
			self.columns = 5

		if self.difficulty == 'medium':
			self.rows = 10
			self.columns = 10

		if self.difficulty == 'hard':
			self.rows = 12
			self.columns = 12

		# Set up the spot list with a loop
		# spot_list[row letter][column number]
		for counter in range(self.rows):
			new_row = []

			for counter2 in range(self.columns):
				spot = Spot()
				new_row.append(spot)

			self.spot_list.append(new_row)
		# end of spot list init

	def get_spot(self, letter, number):
		letter_index = self.letter_list.index(letter)
		return self.spot_list[letter_index][number-1]

	def place_shot(self, letter, number):
		letter_index = self.letter_list.index(letter)
		spot = self.spot_list[letter_index][number-1]
		spot.has_shot = True

	def place_boat(self, letter, number):
		letter_index = self.letter_list.index(letter)
		spot = self.spot_list[letter_index][number-1]
		spot.has_boat = True

	def draw_board(self):

		# print the column numbers
		top_row = '  '
		for counter in range(self.columns):
			top_row += '  ' + str(counter +1) + '  '
		print top_row


		# typing letter_list[2] gives us "C"

		# here we want to loop through all of the columns on the board
		for counter in range(self.rows):

			# Print the letter of the row first
			one_row = self.letter_list[counter]

			for counter2 in range(self.columns):
				spot = self.spot_list[counter][counter2]
				one_row += spot.print_spot()
			print one_row

	# TODO make a function to check if there are empty sapces left
	# we can use this to end the program if there are no more spaces
