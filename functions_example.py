#functions example

import random


# Make the function
def getSomeRandomNumbers(amount_of_numbers):

	list_of_random_numbers = []

	for counter in range(amount_of_numbers):
		new_number = random.randint(0, 100000000)
		list_of_random_numbers.append(new_number)

	return list_of_random_numbers







# Use the functions
my_list = getSomeRandomNumbers(100)
print my_list





