chars = ' abcdefghijklmnopqrstuvwxyz'

"""
  #NOTE
	Dr Mohammed Kamal we included the white-space as a char in this code
	so its going to became a letter after the encryption
"""

plainText = input('Enter the text: ').lower()
key = input('Enter the key: ').lower()


def encrypt(key, text):
	newText = ""
	for i in range(len(text)):
		targetIndex = chars.index(text[i]) + chars.index(key[i%len(key)])
		newText += chars[targetIndex%27]
	print(f"'{newText}'")

def decrypt(key, text):
	newText = ""
	for i in range(len(text)):
		targetIndex = chars.index(text[i]) - chars.index(key[i%len(key)])
		newText += chars[targetIndex%27]
	print(f"'{newText.upper()}'")

# if condtion to select the function
x = int(input("1 for encryption & 2 for decryption: "))
if x == 1:
	encrypt(key, plainText)
else:
	decrypt(key, plainText)