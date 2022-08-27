# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

i=1
while i<=5:
    j=1
    a=0
    k=0
    while j<=i:
        print(i+k,end=" ")
        j+=1
        a+=1
        k=k+5-a
    i+=1
    print()


