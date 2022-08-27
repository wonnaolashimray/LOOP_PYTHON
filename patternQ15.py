# 1
# 2 3
# 4 5 6
# 7 8 9 10

i=1
sum=1
while i<=4:
    j=1
    while j<=i:
        print(sum,end=" ")
        sum+=1
        j+=1
    print()
    i+=1
