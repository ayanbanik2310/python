class phone:
    
    manufactured = 'china'
    
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
    
    def send_sms(self, phone , sms):
        text = f'sending sms to: {phone}  and message {sms}'
        print(myphone.owner)
        return text
    
if __name__ == '__main__':
    myphone = phone('ayan banik', 'samsung', '17500')
    
    print(myphone.owner, myphone.brand, myphone.price)

    text = myphone.send_sms(123, 'ayan is a good boy')
    print(text)


    her_phone = phone('she', 'redmi', 13000)
    print(her_phone.owner, her_phone.price, her_phone.brand)
    