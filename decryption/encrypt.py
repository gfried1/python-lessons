class Encrypt(object):

	def __init__(self):
		# set properties and option
		self.thing = 'thing'
		self.base_number = 17

	def encrypt(self, unchanged_sentence):

		changed_sentence = ''

		length = len(unchanged_sentence)

		for counter in range(length):
			number = ord(unchanged_sentence[counter])
			#print number
			changed_sentence = changed_sentence + ' ' + str(number)
		
		
		# encrypt stuff!
		# changed_sentence is something like "34 95 46 569 113 459 96"
		return changed_sentence

	
	def decrypt(self, string_of_numbers): # this is 1. take in one variable as a parameter (which is the string of numbers)


    # 2. turn the string of numbers into a python list of numbers
		number_list = string_of_numbers.split() # .split() is what turns this into a list
		


		decrypted_message = '' # we will use this to save each letter as we convert numbers into letters

		for number in number_list:
			# 3. convert this number into a letter
			num = int(number)
			letter = chr(num)

			# 4. add the letter to our decrypted_message string
			decrypted_message += letter


		return decrypted_message


