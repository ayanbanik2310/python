def call():
    print('calling someone i don\'t know')
    return 'call done'

class phone:
    price = 17500
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'mic']

    def call(self):
        print('calling class person')

    def send_sms(self, phone , sms):
        text = f'sending sms to: {phone}  and message {sms}'
        return text

myphone = phone()
print(phone().features)
call()
myphone.call()
text = myphone.send_sms(123 ,'ayan is a good boy')
print(text)