class calculator:
    brand = 'casia'
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addision(self):
        return self.num1+self.num2
    def subtraction(self):
        return self.num1 - self.num2
    def multiplication(self):
        return self.num1* self.num2
    def division(self):
        return self.num1 / self.num2

if __name__ == '__main__':
    num1 = int(input('enter number 1 : '))
    num2 = int(input('enter number 2 : '))
    print('option 1 : addition')
    print('option 2 : multiplication')
    print('option 3 : substraction')
    print('option 4 : division')
    n = int(input('choose and option : '))

    mycalcu = calculator(num1, num2)
    if n==1:
        ans = mycalcu.addision()
        print('your ans is : ', ans)
    elif n==2:
        ans = mycalcu.multiplication()
        print('your ans is : ', ans)
    elif n==3:
        ans = mycalcu.subtraction()
        print('your ans is : ', ans)
    elif n==4:
        ans = mycalcu.division()
        print('your ans is : ', ans)
    else:
        print('you entered wrong option, khatam geya bye bye')
    
