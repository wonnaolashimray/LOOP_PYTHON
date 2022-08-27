a=float(input('marks in physics(out of 100) = '))
b=float(input('marks in chemistry(out of 100) = '))
c=float(input('marks in maths(out of 100) = '))
d=float(input('marks in biology(out of 100) = '))
e=float(input('marks in computer(out of 100) = '))
total_marks=500
per_of_a=a/500*100
per_of_b=b/500*100
per_of_c=c/500*100
per_of_d=d/500*100
per_of_e=e/500*100
per_of_all=per_of_a+per_of_b+per_of_c+per_of_d+per_of_e
if per_of_all>=90:
    print('percentage =',round(per_of_all),'%','\ngrade = Grade A')
elif per_of_all>=80:
    print("percentage =",round(per_of_all),"%",'\ngrade = Grade B')
elif per_of_all>=70:
    print('percentage =',round(per_of_all),'%',"\ngrade = Grade C")
elif per_of_all>=60:
    print('percentage =',round(per_of_all),'%','\ngrade = Grade D')
elif per_of_all>=40:
    print('percentage =',round(per_of_all),'%','\ngrade = Grade E')
else:
    print('percentage =',(round(per_of_all)),"%","\ngrade = Grade F")
