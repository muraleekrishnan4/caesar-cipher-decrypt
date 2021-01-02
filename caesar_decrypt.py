#Ceaser Cipher Decrypt
#Author : Muraleekrishnan
#Date : 02-Jan-2021

#defining alphabets
alphabets = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"



def decrypt():
	
	#print Welcome message
	print("\nCeaser Cipher Decrypter")
	print("************************")


	#read user input
	cText = input("\nEnter the string to decrypt : ")
	key = int(input("Enter to key [shift value] : "))

	pText = ""

	#decrypting
	for char in cText:
		if char.lower() in alphabets:
			#converts uppercase chars
			if char.isupper():
				index = alphabets.index(char.lower())
				index = (index - key)%26
				pText += alphabets[index].upper()
			#converts lowercase char
			else:
				index = alphabets.index(char)
				index = (index - key)%26
				pText += alphabets[index]
		#converts numbers
		elif char in numbers:
			index = numbers.index(char)
			index = (index - key)%10
			pText += numbers[index]
		else:
			pText+=char


	print("\nSuccessfully Decrypted the Cipher!!!")
	print("\nPlain Text : ", pText,"\n")



decrypt()
