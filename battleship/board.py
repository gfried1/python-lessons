class Board(object): 

	def __init__(self, difficulty):
		self.difficulty = difficulty

		self.rows = None
		self.columns = None

		if self.difficulty == 'easy':
			self.rows = 5
			self.columns = 5

		if self.difficulty == 'medium':
			self.rows = 10
			self.columns = 10

		if self.difficulty == 'hard':
			self.rows = 12
			self.columns = 12


		self.title = 'the board'


		# Set up the choice list with a loop
		self.choice_list = []
		for counter in range(self.rows):
			new_row = []

			for counter2 in range(self.columns):
				new_row.append(0)

			self.choice_list.append(new_row)

		print self.choice_list

		self.letter_list= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]


	def draw_board(self):

		# print the column numbers
		top_row = '  '
		for counter in range(self.columns):
			top_row += '  ' + str(counter +1) + '  '
		print top_row


		# typing letter_list[2] gives us "C"

		# here we want to loop through all of the columns on the board
		for counter in range(self.rows):

			one_row = self.letter_list[counter] 
                         
			for counter2 in range(self.columns):
				
				if self.choice_list[counter][counter2] == 0:
					one_row += ' [ ] '	
				else:
					one_row += ' [x] '

			print one_row

		# def place_marker(self):
		# 	

	def draw_boats(self, boat_list):

		print boat_list

		print ' BOAT BOARD '
		# print the column numbers
		top_row = '  '
		for counter in range(self.columns):
			top_row += '  ' + str(counter +1) + '  '
		print top_row


		# typing letter_list[2] gives us "C"

		# here we want to loop through all of the columns on the board
		for counter in range(self.rows):

			one_row = self.letter_list[counter] 
                         
			for counter2 in range(self.columns):

				row_letter = self.letter_list[counter]
				col_number = counter2

				boat_in_list = False
				for boat in boat_list:
					if row_letter == boat.letter and col_number == boat.number:
						boat_in_list = True
						
				if boat_in_list is True:
					one_row += ' [y] '		
				else:
					one_row += ' [ ] '

			print one_row

		# def place_marker(self):
		# 	



	def mark_spot(self, row_letter, col_number):

		print row_letter + str(col_number)

		row_number = self.letter_list.index(row_letter)

		self.choice_list[row_number][col_number-1] = 1
		
		self.draw_board()

	# TODO make a function to check if there are empty sapces left
	# we can use this to end the program if there are no more spaces















