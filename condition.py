# in, not, not in, is is not
# and, or

a = int(input('enter your marks : '))

if(a<0 or a>100):
    print('enter a valid number')
elif a>=80:
    print('A+, excelent result')
elif a>=70:
    print('A, very good')
elif a>=60:
    print('B, good')
elif a>=50:
    print('B-, you have to improve')
elif a>=40:
    print('C, you have to study more')
else:
    print('F, you failed')
