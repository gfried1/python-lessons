# Instructions
#
#
# 1. Run this file!
# 2. Add comments this file!
# 3. Make a loop that prints everything in a list, even if you don't know how many things are in the list.
#      -   How can you determine in python how many things are in a list.
# 
# 
# 6. Add Comments
#
#
#
#
#
#
#
#
#
#
#


print('---------------------------------------')
print('Pizza Activity')
print('---------------------------------------')
print('')

print('Before we learn any more about programming, how about we make a pizza?')
print('We need to choose some pizza toppings for our pizza')


#
menu = ['cheese', 'mushrooms', 'sausage', 'onions', 'pepperoni', 'spinich']



print('Do you want to see the menu?')
raw_input()

#
print('-----------------')
print('Toppings Menu')
print('-----------------')

for counter in range (6):
	print menu[counter]






# make a list.
our_toppings = []




#
print('You should choose 3 toppings for your pizza.')
print('Type in the first topping for your pizza...')
menu_choice = raw_input()
our_toppings.append(menu_choice)

print('Type in the second topping for your pizza...')
menu_choice = raw_input()
our_toppings.append(menu_choice)

print('Type in the third topping for your pizza...')
menu_choice = raw_input()
our_toppings.append(menu_choice)

#
print('You have chosen:')
print(our_toppings[0])
print(our_toppings[1])
print(our_toppings[2])


#
print('')
print('Sorry, we are out of ' + our_toppings[1] + '. Please choose a different topping.')

#
our_toppings.pop(1)

print('Type in a topping for your pizza...')
new_topping = raw_input()

#
our_toppings.insert(1, new_topping)


#
print('Now your pizza has:')
for counter in range(len(our_toppings)):
	print(our_toppings[counter])


#
print('Oh no! It looks like you only have enough money for 2 toppings.')
print('Please the name of the topping you want to remove...')
topping_to_remove = raw_input()
our_toppings.remove(topping_to_remove)

#
print('')
print('Thank you. Now your pizza has:')
for topping in our_toppings:
    print(topping)


# The end
print('')
print('Press any key to end the program')
raw_input()

print('')
print('End of Program')



'''
Module 3 Lesson:




'''
