a=int(input('first side of triangle\n'))
b=int(input('second side of triangle\n'))
c=int(input('third side of triangle\n'))
if a+b>=c and b+c>=a and c+a>=b:
    print('valid')
else:
    print('not valid')    