n=5
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            print(chr(64+i),end=" ")
        else:
            print(i,end=" ")
        j+=1
    print()
    i+=1

        