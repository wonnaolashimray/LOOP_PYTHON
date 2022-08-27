string="python"
length=len(string)
i=1
while i<=length:
    j=0
    while j<i:
        print(string[j],end="")
        j+=1
    i+=1
    print()