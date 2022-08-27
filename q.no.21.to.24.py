a=int(input('enter number'))
if a%2==0 and a%5==0:
    print('tea and coffe')
elif a%2==0:
    print('tea')
elif a%5==0:
    print('coffe')  
else:
    print('ras') 


a=int(input(' no of girls..... ')) 
b=int(input('no of maggi......')) 
if a==b:
    print('both equal')
elif a-b>0: 
    print(a-b,'girls is extra')
    print(a-b,'maggi is less')
else:
    print(b-a,'girls is less')
    print(b-a,"maggi is more")   

a=int(input('enter units'))
if 0<=a>=50:
    print(a*20/100+a*0.50,'Rs')
elif 50<a>=150:
    print(a*20/100+a*0.75,"Rs") 
elif 150<a>=250:
    print(a*20/100+a*0.20,'Rs')
else:
    print(a*20/100+a*1.50,"Rs")  
     
a=int(input('enter total cost of quantity'))
if a<1000:
    print(a,'Rs','No Discount')
else:
    print('Original Cost=',a)
    print(a-a*10/100,"Rs","With 10% Discount")    
   
a=int(input('enter marks'))
if 1<=a<=25:
    print('Grade=F')
elif 25<a<=45:
    print('Grade=E')  
elif 45<a<=50:
    print('Grade=D')
elif 50<a<=60:
    print('Grade=C')  
elif 60<a<=80:
    print('Grade=B') 
elif 80<a<=100:
    print('Grade=A')  
else:
   print('pls enter Marks between 1 to 100') 

a=int(input('enter your salary '))
b=int(input('enter your year/s of service '))
if a>=5:
    print(a+a*5/100,'Rs','with 5% bonus')
else:
    print(a,'Rs')

a=int(input('enter age of one people'))
b=int(input('enter age of second people'))
c=int(input('enter age of third people'))
if a==b>c: 
    print('aged of',a,",",b,"persons is oldests")
    print('aged of',c,'person is youngest')
elif a==b<c:
     print('aged of',c,"persons is oldests")
     print('aged of',a,",",b,'person is youngest')
elif b==c>a:
    print("aged of",b,",",c,'persons is oldests')
    print('aged of',a,"prson is youngest") 
elif b==c<a:
    print("aged of",a,'persons is oldests')
    print('aged of',b,",",c,"prson is youngest") 
elif c==a>b:
    print('aged of',c,",",a,"persons is oldests") 
    print('aged of',b,"person is youngest") 
elif c==a<b:
    print("aged of",b,'persons is oldests')
    print('aged of',c,',',a,"prson is youngest")         
elif a>b>c:
    print('aged of',a,'person is oldest')
    print('aged of',c,'person is youngst')
elif b>c>a:
    print('aged of',b,'person is oldest')    
    print('aged of',a,'person is youngest')
elif c>a>b:
    print('aged of',c,'person is oldest') 
    print('aged of',b,'person is youngest') 
elif b>a>c:
    print('aged of',b,"person is oldest")   
    print('aged of',c,'prson is youngest')  
elif c>b>a:
    print('aged of',c,"person is oldest")    
    print('aged of',a,"person is youngst") 
else:
    print('aged of',a,"person is oldest")
    print('aged of',b,"person is youngest")

