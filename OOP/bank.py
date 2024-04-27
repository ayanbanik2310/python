class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

        self.min_deposit = 1000

    def get_balance(self):
        print('your current balance is', self.balance)
        print()
        return
    
    def deposit(self, amount):
        if amount>=self.min_deposit:
            self.balance = self.balance + amount
            print('deposit successfull')
            print('your current balance is : ', self.balance)
            print()
            return
        else:
            print('unsufficient amount')
            print()
            return
    
    def withdraw(self, amount):
        if amount>=self.min_withdraw and amount<=self.max_withdraw and amount<=self.balance:
            self.balance = self.balance - amount
            print('withdraw successfull')
            print('your current balance is : ', self.balance)
            print()
            return
        else:
            print('insufficent balance')
            print()
            return

if __name__ == '__main__':
    bank1 = bank(1000000)
    while True : 
        print('option 1 : deposit')
        print('option 2 : withdraw')
        print('option 3 : check balance')
        print('option 4 : stop application')
        opt = int(input('choose an option : '))
        
        if opt == 1:
            print(f'you can\'t deposit less than {bank1.min_deposit}')
            amount = int(input('enter amount you want to deposit : '))
            bank1.deposit(amount)

        elif opt == 2:
            print(f'you can\'t withraw less than {bank1.min_withdraw}')
            amount = int(input('enter amount you want to withdraw : '))
            bank1.withdraw(amount)

        elif opt == 3:
            bank1.get_balance()

        elif opt == 4:
            break

        else:
            print('you choose wrong option')

        