
character=input("Enter the letter\n")
if character>='A' and character<='Z':
	print("UPPER letter")
elif character>='a' and character<='z':
	print("LOWER CASE")
elif (int(ord(character))>=48 and int(ord(character))<=57):
	print("number")
else:
	print("SPECIAL CASE")
