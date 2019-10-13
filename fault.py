print("enter the numbers")
n1=int(input())
n2=int(input())
print("which operation you want to performe /,*,+,-")
operation=input()
if n1==45 and n2==3 and operation=="*":
	print(777)
elif n1==56 and n2==9 and operation=="+":
	print(877)
elif n1==56 and n2==6 and operation=="/":
	print(4)
elif n1==56 and n2==5 and operation=="-":
	print(12)
elif operation=="*":
	output=n1*n2
	print(output)
elif operation=="/":
	output=n1/n2
	print(output)
elif operation=="+":
	output=n1+n2
	print(output)
elif operation=="-":
	output=n1-n2
	print(output)
else:
	print("invalid output")

