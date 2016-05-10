#Fish tank

from fish import Fish


fish_list = []

for counter in range(100):
	new_fish = Fish('g' + str(counter)) 
	fish_list.append(new_fish)



for counter in range(100):
	one_fish = fish_list[counter]
	one_fish.move_random()



for counter in range(100):
	# get a fish form the list
	one_fish = fish_list[counter]

	# make that fish say its name
	one_fish.say_name()
