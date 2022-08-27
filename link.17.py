#write a python program to calculate profit and lost.
print('To claculate profit and loss  in percentage enter some detail below ')
a=float(input('cost price'))
b=float(input('selling price'))
if a>b:
    print('profit =',(round(((a-b)/a)*100)),"%")
elif b>a:
    print('loss =',(round(((b-a)/a)*100)),"%")
else:
    print('no profit no loss')


