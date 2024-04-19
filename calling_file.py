
balance = 5000

def add_kor(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum
    
""" if __name__ == '__main__':  this line means , main function will only call if we run this file runs 
if we don't use this lines and we called this files from others files the whole code will be run """

if __name__ == '__main__':       
      
    ans = add_kor(10,20,30)
    print(ans)
    balance = balance - ans
    print(balance)