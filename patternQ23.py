# 1
# 4 9
# 16 25 36
# 49 64 81 100

# i=1
sum=1
while i<=4:
    j=1
    while j<=i:
        print(sum*sum,end=" ")
        sum+=1
        j+=1
        
    print()
    i+=1

