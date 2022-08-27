a=int(input('date'))
b=int(input('month'))
c=int(input('year'))
if 1<=a<31 and b!=2 and b!=4 and b!=6 and b!=9 and b!=11:
   print(a+1,'-',b,"-",c)
elif 1<=a<=31 and b!=12:
    print(1,"-",b+1,"-",c)      
else:
    print(1,"-",1,"-",c+1) 

a=int(input('table of = '))
print("\n",a,'x 1 =',a,"\n",a,"x 2 =",2*a,"\n",a,'x 3 =',3*a,"\n",a,'x 4 =',4*a,"\n"\
,a,'x 5 =',5*a,"\n",a,'x 6 =',6*a,"\n",a,'x 7 =',7*a,'\n',a,'x 8 =',8*a,'\n',a,'x 9 =',9*a,"\n",a,"x 10 =",10*a) 

a=input('enter ')
b=len(a)
if b>=3 and a[-1]=='g' and a[-2]=='n' and a[-3]=='i':  
           print(a +"ly")
elif b>=3:
    print(a+"ing")         

a=int(input('enter a number'))
if 0<=a<=100:
    print('this is within 100')
elif 100<a<=1000:
    print('this is within 1000') 
elif 1000<a<=2000:
    print('this is within 2000') 
else:
    print('this is not within 100,1000,2000')
  


