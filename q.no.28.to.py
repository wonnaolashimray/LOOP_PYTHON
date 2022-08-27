a=int(input('ente your age '))
if a>=18:
    print('you are aligible for voting')
elif a<=0 or a>150:
    print('pls enter your real age') 
else:
    print('you are not eligible to give vote')       

a=int(input('enter number'))
if a%7==0:
    print(a,'is divisible by 7')
else:
    print(a,'is not divisible by 7')

a=int(input('enter a number'))
b=a%10
if b%3==0:
    print(b,"is divisible by 3")
else:
    print(b,'is not divisible by 3')    

a=int(input('enter cost of bike'))
if a<=50000:
    print("road tax =",a*5/100)
elif 50000<a<=100000: 
    print('road tax =',a*10/100) 
else:
    print('road tax =',a*15/100)    

a=int(input('your age '))
if a>=60:
    print('sineor citizen')
else:
    print('not senior citizen')    

a=int(input('enter no. '))
if 100<=a<=999:
    print('this is three digit number')
else:
    print('this is not three digit number')    

a=int(input('enter no.'))
b=int(input('enter no.'))
c=(input('enter operation'))
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)  
elif c=='*':
    print(a*b)   
elif c=="/":
    print(a/b)
elif c=='%':
    print(a%b) 
elif c=="//":
    print(a//b)
elif c=="**":
    print(a**b) 
else:
    print("enter mathmatical operation")                   

a=int(input('enter days'))
if 1<=a<=5:
    print(2*a)
elif 5<a<=10:
    print((a-5)*3+10)
elif 10<a<=15:
    print(10+15+(a-10)*4) 
elif a>15:
    print(((a-15)*5)+10+15+20)   

a=int(input('enter a number'))
if 1500<=a<=2700:
    if a%7==0 and a%5==0:
        print(a,"is divisible by 7 and also multiple of 5")
    else:
        print(a,"is not divisible by 7 nor multiple of 5")   
else:
    print('enter number between 1500 to 2700')      

   
number=5
a=int(input('guess number between 1-9 '))
if a==5:
    print('correct')
elif a>9:
    print('pls enter number bertween 1-9 ')    
else:
    print('incorrect')    

a=int(input('enter number '))
b=int(input('enter number '))
if 15<=(a+b)<=20:
    print(20)
else:
    print(a+b)  
  
       
a=int(input('enter day'))
b=int(input('enter month'))
if 3<=b<=5:
    print('spring season')
elif 6<=b<=8:
    print('summer season')
elif 9<=b<=11:
    print('autumn season')    
elif b==12 or 1<=a<=2:
    print('winter season')    
else:
    print('pls enter month batween 1-12')


