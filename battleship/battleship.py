#battleship 

"""
things needed:
board
	grid
pieces
	ships
	pegs
game loop
	need to make a loop that runs the game round after round 
players
win condition
	sink all their battleships by putting your pegs where their battleships are
	switching off
	computer needs to randomize its selection and the person will chose a spot and the computer will tell them if it is where one of their battleships are
	
"""


# Old battleship code

print "You ran the wrong file, run battleship_game.py instead."

"""
from board import Board


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

print "choose a board (easy, medium or hard)"


difficulty_level = raw_input()

if difficulty_level == '':
	difficulty_level = 'easy'



board = Board (difficulty_level)
board.draw_board()

board_in_action = True

while board_in_action is True:

	good_choice = False

	while good_choice is False:
		print "write the place you want to hit (capitol letter than number no spaces). Type 'end' to quit."
		player_chose = raw_input()  # Expected input: numberletter 
		if player_chose != '':
			# player_chose[0] is the letter, player_chose[1:] is the rest of the number
			if player_chose == 'end' or (player_chose[0] in board.letter_list and int(player_chose[1:]) in range(13)): # if its a letter then number
				good_choice = True


	# Check to see if they typed a letter then number.

	if player_chose != 'end':
		row_letter = player_chose[0]   #  'A'
		col_number = int(player_chose[1:]) # 3
		board.find_spot(row_letter, col_number)
	else:
		board_in_action = False
		




print '------------'
print 'end'
print '------------'


"""
