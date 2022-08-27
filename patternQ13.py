i=1
while i<=5:
    j=1
    while j<=i:
        if j%2!=0:
            print(i,end=" ")
        else:
            print("*",end=" ")
        j+=1
    print()
    i+=1
