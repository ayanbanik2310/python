# example 1

def double_it(num):
    result = num * 2
    return result

n = 10
x = double_it(n)
print(x)


#example 2

def add_kor(a,b):
    # result = a+b
    # return result
    return (a+b)


a = int(input())
b = int(input())

sum = add_kor(a,b)
print(sum)


# example 3

def sum(a=0,b=0,c=0):
    return (a+b+c)

a=10
b=20
c=30
ans = sum(a)
print(ans)
ans = sum(a,b)
print(ans)
ans = sum(a,b,c)
print(ans)


# example 4 : args 
# unknown number of parameters, 
# def funtion(*args)


def all_sum(*numbers):
    # print(numbers)
    sum = 0
    for num in numbers:
        print(num, end=' ')
        sum = sum + num
    print()
    return sum

total = all_sum(45,60,100,95)
print(total)


# example 5 
# advanced kargs
# multiple return from function

def multi_return (a,b):
    sum = a+b
    multi = a*b
    dif = a-b
    #return [sum, multi, dif]       # return as a list
    return sum, multi, dif         # return as a tuple

everything = multi_return(50,20)
print(everything)


#example 6
# global variable and function
# if you want to use global variable inside a function you have to use global keyword
# you can use global variable without global keyword , but if you do so you can't use the value globally declared
# you can't use a varible , that you delared inside a function

balance = 5000             # global variable

def expense(items, price):
    dream_phone = 'iphone'
    global balance                # using global keyword to access global varible
    # balance = 500                   # local balance variable 
    balance = balance - price
    print('balance inside function ', balance)

# print(dream_phone)                       # local varible , declared inside expense function
print('balance before buy ', balance)
expense('chosma', 500)
print('balance after buy ', balance)

