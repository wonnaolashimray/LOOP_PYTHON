i=5
while i>=1:
    j=1
    while j<=i:
        if i%2==0:
            print("*",end=" ")
        else:
            print(i,end=" ")
        j+=1
    print()
    i-=1