    # python data structure 
    # https://docs.python.org/3/tutorial/datastructures.html


if __name__ == '__main__':
    # index    0    1   2   3   4   5  6  7  8  9
    numbers = [45, 54, 56, 65, 12, 21, 3, 2, 8, 7]
    # index    -10 -9  -8  -7  -6  -5 -4 -3 -2 -1
    print(numbers[1], numbers[5])
    print(numbers[-1], numbers[-5])
    sum = 0
    print('all elements of numbers are : ', end='')
    for i in range(len(numbers)):
        print(numbers[i], end=' ')
        sum = sum + numbers[i]
    print()
    print('sum = ', sum)

    # list_name[start : end]
    print(numbers[2 : 9])      # it will print from 2nd index to 8th index

    # list_name(start : end : steps)   
    print(numbers[1 : 8 : 2])  # it will print every 2nd number from 1 to 7
    print(numbers[7 : 0 :-2])

    # list_name[start : ]      # it will print from start to the end of the list
    # list_name[ : end]        # it wiil print from 0 and stops before end
    # list_name[ : ]           # it will start from 0 and stops5 at end of the list end
    
    

if __name__ == '__main__':
    print('the end haha')

