#program for simple timing
a=input('enter timing-ex(6:30 Am) :-')
if a=='6 Am': 
    print('morning exercise')
if a=='8 Am':
    print('first coding class')    
if a=='12:30 Pm':
    print('lunch break')  
if a==2:
    print('second coding class')     
if a=='5 Pm':
    print('snack break')     
if a=='6 Pm':    
    print('english activity')
if a=='8 Pm':
    print('dinner break')
else:
    print('time out')

# program for timing
a=input('enter timing = ')  
b=int(a[0:-6])
c=int(a[3:-3])
if  a[2]==":" and a[5]==" ": 
    if (a[6]=="A" or a[6]=="a") and a[7]=="m":
       if b==6 and c==30:
        print("morning exercise,for 07:30 am - 06:30 am")
       elif (b==6 and 60>c>30) or (b==7 and 30>=c>=0):
        print('morning exercise is going on,06:30 am - 07:30 am')
       elif b==8 and c==0:
        print('1st coding class,08:00 am - 12:30 pm')
       elif (12>b>=8 and 60>c>=0):
        print('1st coding class is going on,08:00 am - 12:30 pm')
       else:
        print('no class,no activity')
    if (a[6]=='P' or a[6]=="p") and a[7]=='m':
       if b==12 and 30>c>=0:
        print('1st coding class is going on,08:00 am - 12:30 pm')
       elif b==12 and c==30:
        print('lunch break,12:30 pm - 02:00 pm') 
       elif (b==12 and 60>c>30) or (b==1 and 60>c>=0):
        print('lunch break is going on,12:30 pm - 02:00 pm')
       elif b==2 and c==0:
        print('2nd coding class,02:00 pm - 05:00 pm')   
       elif 5>b>=2 and 60>c>=0:
        print('2nd coding class is going on,02:00 pm - 05:00 pm') 
       elif b==5 and c==0:
        print('snack break,05:00 pm - 06:00 pm')        
       elif b==5 and 60>c>0:
        print('snack break is going on,05:00 pm - 06:00 pm')   
       elif b==6 and c==0:
        print('english activity,06:00 pm - 08:00 pm')    
       elif 8>b>=6 and 60>c>=0:
        print('english activity is going on,06:00 pm - 08:00 pm')
       elif b==8 and c==0:
        print('dinner break,is after 08:00 pm') 
       elif 9>=b>=8 and 60>=c>=0:
        print('dinner break is going on,is after 08:00 pm')
       elif c==60:
        print("please enter valid time,hence '00:60 Am/Pm' is not valid") 
       else:
        print('timing off(no class,no activity)')
else:
    print('plese check is there space between timing and am/pm or not')
    print("Or put ':' between hours and minute")  
#program for
a=input('enter your council post ')
if a=='fc' or a=='Fc' or a=='Fc' or a=='fC' or a=='Food cordinator' or a=='Food Cordinator':
    print('Fc=Nikita and Sminao\nwork of fc=food managment,grocessy managment')
if a=="disco" or a=="DISCO" or a=="Disco" or a=='Displine cordinator' or a=='DisckPad-E14:~/Desktop$pline Cordinator':
    print('Disco=Rajeshwari and warshimla\nwork of disco=manage displine and culture,check all girls coming on tim in classroom or not') 
if a=="Health cordinator" or a=="Health Cordinator":
    print('Health Cordinator=karishma\nwork of Health Cordinator=take care of sick girls') 
if a=='tresarer' or a=='Tresarer' or a=='TRESARER':
    print('Tresarer=Praharshita\nwork of Tresarer=finacial managemnt')  
if a=="Facility maintenance" or a=='Facility Maintainance' or a=='facility maintainance' or a=="fm" or a=='FM' or a=='Fm':
     print('Facility maintanance=onring and chunkham\nprovide facility of beds and and  provide all cleaning item') 
if a=='Outreach' or a=='OUTREACH':
    print('Outreach=Taresa\nwork of outreach=entertainment manage and manage social account of Ng') 
if a=='Training and placement' or a=="Training And Placment": 
    print('TnP=Grace and Anisha\nwork of TnP=taken interview,education facilator and provide mentor')
if a=="Information Technology" or a=='Information technology' or a=='IT' or a=='It':
    print('IT=Suvarna\nWork of IT=technology work faccilator and laptop provide')     

a=input('enter your language,e(enter in capital latters---')
cu_balance=10000
if a=='ENGLISH':
    print('welcome to SBI Bank')
    b=int(input('enter pin.....'))
    if b==1234:
      print('enter your card..') 
      c=input('choose an option\n1.-withdraw\n2.balance enguery\n3.diposit\n4.exit\n')
      if c=='4':
        print('thanks for coming')
      if c=='3':
        print('how many you want deposit.....')
        d=int(input('enter amount'))
        print('your current balace is =',cu_balance+d)
        print('thanks for visit') 
      if c=='2':
       print('your current balance is =',cu_balance)
       print('thanks for visit') 
      if c=='1':
          e=int(input('enter money you want withdraw'))
          if e>cu_balance:
              print('your balance is less than you entered')
          else: 
              print('your current balance is =',cu_balance-e)
              print('thanks for visit') 
    else:
        print('incorrect,try again')      
