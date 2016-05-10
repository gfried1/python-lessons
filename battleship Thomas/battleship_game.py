
from board import Board

class BattleshipGame(object):


	def __init__(self):
		self.start()
		self.board_selection()
		self.boat_selection()

		self.board_in_action = True

		while self.board_in_action is True:
			self.take_a_turn()

		self.print_end()

	def start(self):
		print '------------'
		print 'start'
		print '------------'

		#let the user type something:
		print "type your name"

		#lets them type: Raw input
		name = raw_input()

		if name == '':
			name = 'Garrett'

		# Do different things based on what the user typed
		if name == "Garrett":

			print "hello Garrett"

		if name != "Garrett":

			print name

	def board_selection(self):
		print "choose a board (easy, medium or hard)"

		difficulty_level = raw_input()

		if difficulty_level == '':
			difficulty_level = 'easy'

		self.board = Board (difficulty_level)
		self.board.draw_board()

	def boat_selection(self):
		self.boats = []
		for counter in range(4):
			boat_length = counter + 2

			message = "type the coordinates you want your boat to go (capitol letter then number no spaces for the coordinates) " + str(boat_length) + " this is the length of your boat"
			spot = self.choose_spot(message)

			self.board.place_boat(spot[0], spot[1])
			self.board.draw_board()

		#print self.boats



	def take_a_turn(self):
		message = "write the place you want to hit (capitol letter then number no spaces). Type 'end' to quit."
		spot = self.choose_spot(message)
		if spot is None:
			return None

		self.board.place_shot(spot[0], spot[1])
		self.board.draw_board()


	def choose_spot(self, message):
		good_choice = False
		while good_choice is False:
			print message
			player_chose = raw_input()  # Expected input: numberletter
			good_choice = self.validate(player_chose)

		# Check to see if they typed a letter then number.

		if player_chose != 'end':
			row_letter = player_chose[0]   #  'A'
			col_number = int(player_chose[1:]) # 3
			return [row_letter, col_number]

		else:
			self.board_in_action = False
			return None


	def validate(self, player_chose ):

		if player_chose != '':
			# player_chose[0] is the letter, player_chose[1:] is the rest of the number
			if player_chose == 'end' or (player_chose[0] in self.board.letter_list and int(player_chose[1:]) in range(13)): # if its a letter then number
				return True

		return False

	def print_end(self):
		print '------------'
		print 'end'
		print '------------'



BattleshipGame()
