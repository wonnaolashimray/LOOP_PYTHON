#write a program to find triangle is equilateral or isoseles or scalenene. 
a=int(input('first angle of triangle\n'))
b=int(input('second angle of triangle\n'))
c=int(input('third angle of triangle\n'))
if a==60 and b==60 and c==60:
    print('equalateral')
elif a==b or b==c or c==a:
    print('isocele')
else:
    print('scalene')