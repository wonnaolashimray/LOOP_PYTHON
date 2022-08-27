# 5 10 15 20 25 
# 4 9  14 19 24 
# 3 8  13 18 23 
# 2 7  12 17 22 
# 1 6  11 16 21 

n=5
i=0
while i<n:
    k=n-i
    j=0
    while j<n:
        print(k,end=" ")
        k+=5
        j+=1
    i+=1
    print()
