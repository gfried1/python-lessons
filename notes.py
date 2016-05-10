#notes

"""

cd change directory


ls list stuff

python (file name).py


"""

print '------------'
print 'start'
print '------------'

# Make a variable
thing = 10 # thing is now a variable

#let the user type something:  
print "type your name"

#lets them type: Raw input
name = raw_input()


# Do different things based on what the user typed
if name == "Garrett":

	print "hello Garrett"

if name != "Garrett":

	print name


# Here's an example of a for loop
for letter in name:
	print ' - ' + letter

difficulty_level= 'easy'
difficulty_level= 'medium'
difficulty_level= 'hard'


board= Board (difficulty_level)



print '------------'
print 'end'
print '------------'