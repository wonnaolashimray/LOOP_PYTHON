n=int(input(" enter any number"))
sum=0
i=n
while i>0:
    r=i%10
    sum=sum+r
    i=i//10
if n%sum==0:
    print(n,"is harshad number")
else:
    print(n,"is not harshad number")