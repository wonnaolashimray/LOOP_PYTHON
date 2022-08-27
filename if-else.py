speed=int(input('car spped='))
if speed<=60:
    print('limited speed')
else:
    print('overspeeding')

a=input('enter letter')
if a=="a" or a=='e' or a=='i' or a=='o' or a=='u':
    print('this is vowel')
else:
    print('this is consonent')

_ch=input('enter character')
if (_ch>='a' or _ch>='A'):
    print('this is an alphabet')
elif ((_ch>='0' and _ch<='-9') or (_ch>='0' and _ch<='9')):
    print('this is digit')
else:
    print('this is a special character')



