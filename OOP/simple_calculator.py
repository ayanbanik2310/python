class calculator:
    brand = 'casia'
    
    def addision(self, num1, num2):
        return num1+num2
    def subtraction(self, num1, num2):
        return num1 - num2
    def multiplication(self, num1, num2):
        return num1 * num2
    def division(self, num1, num2):
        return num1 / num2

if __name__ == '__main__':
    num1 = int(input('enter number 1 : '))
    num2 = int(input('enter number 2 : '))
    print('option 1 : addition')
    print('option 2 : multiplication')
    print('option 3 : substraction')
    print('option 4 : division')
    n = int(input('choose and option : '))

    mycalcu = calculator()
    if n==1:
        ans = mycalcu.addision(num1, num2)
        print('your ans is : ', ans)
    elif n==2:
        ans = mycalcu.multiplication(num1, num2)
        print('your ans is : ', ans)
    elif n==3:
        ans = mycalcu.subtraction(num1, num2)
        print('your ans is : ', ans)
    elif n==2:
        ans = mycalcu.division(num1, num2)
        print('your ans is : ', ans)
    else:
        print('you entered wrong option, khatam geya bye bye')
    
