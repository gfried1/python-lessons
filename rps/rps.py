#rps
#ask person choose: rock, paper or scissors
#computer randomly picks something 
#print what computer chooses and what person chooses
#then say winner
#in terminals: cd is choose directory (folder) ls list stuff

import random
from time import sleep
from scoreboard import Scoreboard
#this is making a new scoreboard
my_score = Scoreboard()
	
computer_score = Scoreboard()

print "lets play rock, paper, scissors"

sleep(0.2)


for counter in range(5): 

	my_list = ["rock", "paper", "scissors"]

	good_choice = False
	while not good_choice:
		#ask player for their choice
		print "choose rock, paper or scissors:"
		player = raw_input()
		if player in my_list:
			good_choice = True
			




	#what cpu choses from list then it randomely selects
	cpu = random.choice(my_list)
	print cpu 


	


	#if the player choses rock and cpu choses scissors print winner


	if player == "rock" and cpu == "scissors": 
		print "winner"
		my_score.add_point()
	if player == "paper" and cpu == "rock":
		print "winner"
		my_score.add_point()
	if player == "rock" and cpu == "paper":
		print "loser"
		computer_score.add_point()
	if player == "scissors" and cpu == "paper":
		print "winner"
		my_score.add_point()
	if player == "paper" and cpu == "scissors":
		print "loser"
		computer_score.add_point()
	if player == "scissors" and cpu == "rock":
		print "loser"
		computer_score.add_point()

		

	print 'my score is:'
	my_score.print_score()

	print 'computer\'s score is:'
	computer_score.print_score()


	if player == cpu:
		print "tie"




score = my_score.get_score()
score2 = computer_score.get_score()

print "your final score is"
print score


print "computer\'s final score is"
print score2


if score > score2:
	print "you win computer loses"



elif score < score2: 
	print "you lost computer wins"



else:
	 print "tie"











