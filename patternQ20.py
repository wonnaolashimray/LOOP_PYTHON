# A F K P U
# B G L Q V
# C H M R W
# D I N S X
# E J O T Y
                 
i=1
k=ord("A")
while i<=5:
    j=k
    while j<=ord("Y"):
        print(chr(j),end=" ")
        j+=5
    i+=1
    k+=1
    print()