# A
# B C
# D E F 
# G H I J
# K L N M O   


i=1
sum=ord("A")
while i<=5:
    j=1
    while j<=i:
        print(chr(sum),end=" ")
        sum+=1
        j+=1
    print()
    i+=1