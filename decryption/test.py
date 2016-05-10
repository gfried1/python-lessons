from encrypt import Encrypt

unchanged_sentence = raw_input('Type some words to encrypt\n')

our_encryptor = Encrypt()


encrypted_text = our_encryptor.encrypt( unchanged_sentence )
print encrypted_text


decrypted_message = our_encryptor.decrypt(encrypted_text)

if decrypted_message == unchanged_sentence:
	print 'it worked'
	print decrypted_message







