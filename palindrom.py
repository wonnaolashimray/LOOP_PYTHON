# write a program to check whether a number is palindrom or not
num=int(input("enter the number"))
temp=num
rev=0
while num>0:
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==rev:
    print("it is a palindrom")
else:
    print("it is not a palindrom")



