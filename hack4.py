n=int(input())
if n%2!=0:
    print("Weird")
elif n%2==0 and n in range (2,5):
    print("Not Weird")
elif n%2==0 and n in range (6,20):
    print("Weird")
else:
    print("Weird")
