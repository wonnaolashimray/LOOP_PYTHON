a=int(input("enter the number"))
i=1
b=0
while i<=a:
    if a%i==0 and a%a==0:
        b+=1
    i+=1
if b==2:
    print("prime number")
else:
    print("not prime number")