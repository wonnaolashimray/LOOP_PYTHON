i=int(input('enter a number'))
if i<15:
    print('i is smaller than 15')
    if i<12:
        print('i is smaller than 12')
        if i<10:
            print('i is also less than 10')
else:
    print('i is greater than 15')

#nested if else
a=5
b=10
c=15
if a<b:
    print('a')
    if a<c:
        print('b')
    else:
        print('c')
    if b>c:
        print('d')
    else:
        print('e')
            