print("please insert your ATM")
print("Welcome to SBI")
pin_code=int(input("enter your pin: "))
balance=50000
pin=1234
if pin_code==pin:
    print("1=cash_withdrawal")
    print("2=balance_enquiry")
    print("3=deposite")
    print("4=pin_generation")
    print("5=exit")
transaction=int(input("enter the number"))
if transaction==1:
    withdrawal=int(input("enter the ammount"))
    if withdrawal<=balance:
        print("collect your cash",withdrawal)
        print("remaining balance",balance-withdrawal)
    else:
        print("not enough cash in your account")
elif transaction==2:
    print("your balance",balance)
elif transaction==3:
    deposit=int(input("enter the number"))
    print("total_ammount",balance+deposit)
elif transaction==4:
    pin_genration=int(input("enter new pin"))
    print("new pin=",pin_generation)
elif transaction==5:
    print("Thank you for visiting")