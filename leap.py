year=int(input("Enter the year\n"))

if year%400==0:
	print("this is leap year")
elif year%4==0 and year%100!=0:
	print("this is leap year")
else:
	print("this is not leap year")

	
