chars = ' abcdefghijklmnopqrstuvwxyz'

"""
  #NOTE
	Dr Mohammed Kamal we included the white-space as a char in this code
	so its going to became a letter after the encryption
"""

file = open('input.txt', 'r')
lines = file.readlines()

otputFile = open('output.txt', 'w')

# plainText = input('Enter the text: ').lower()
key = input('Enter the key: ').lower()


def encrypt(key, text):
	newText = ""
	for i in range(len(text)):
		targetIndex = chars.index(text[i]) + chars.index(key[i%len(key)])
		newText += chars[targetIndex%27]
	# print(f"'{newText}'")
	return newText

def decrypt(key, text):
	newText = ""
	for i in range(len(text)):
		targetIndex = chars.index(text[i]) - chars.index(key[i%len(key)])
		newText += chars[targetIndex%27]
	# print(f"'{newText.upper()}'")
	return newText






# if condtion to select the function
x = int(input("1 for encryption & 2 for decryption: "))
if x == 1:
	for line in lines:
		line = line.strip().lower()
		otputFile.write(encrypt(key, line).upper() + '\n')
	print('file encrypted')
		
else:
	for line in lines:
		line = line.strip().lower()
		otputFile.write(decrypt(key, line).title() + '\n')
	print('file decrypted')
		

