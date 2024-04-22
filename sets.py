# list  --> []
# tuple --> ()
# set   --> {}           # no duplicate, 

if __name__=='__main__':
    numbers = [12,  56, 78, 56, 12, 6, 98]
    numbers_set = set(numbers)
    print(numbers)
    print(numbers_set)
    numbers_set.add(0)
    numbers_set.add(13)
    print(numbers_set)

    for item in numbers_set:
        print(item, end=' ')
    print()

    a = {1, 3, 5, 7}
    b = {1, 2, 3, 4 , 5}
    print(a | b)
    print(a & b)

# take a look for method from python documentation and geeksforgeeks