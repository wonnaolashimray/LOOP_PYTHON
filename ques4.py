# a=int(input('enter a number'))
# b=int(input('enter another number'))
# if a%b==0:
#     print(a,'is divisible by',b)
# else:
#     print(a,'is not divisible by',b)
import re
a=input('enter your password')
if len(a)>=8 and len(a)<=16:
    if re.search('[a-zA-Z]',a):
        if re.search('[0-9]',a):
            if re.search('[!-+]',a):
                print('this is strong password')
            else:
                print('do not strong password') 
        else:
            print('do not strong password') 
    else:
        print('do not strong password')                  
else:
    print('do not strong password')                
