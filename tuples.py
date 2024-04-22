# list   3rd bracket
# touple 1st bracket

def multiple():
    return 1, 3, 4

if __name__ == '__main__' :
    print(multiple())
    things  = 'pen' , 'tripod', 'pencil', 'scale', 1, 2, 3.12       # different types of data can be stored in touples
    print(things)
    print(type(things))

    print(things[1])
    print(things[-1])
    print(things[1:3])
    print(things[1:7:2])

    if 'pen' in things:
        print('exists')
    
    for item in things:
        print(item, end = ' ')
    
    # things[0] = 'fardin'            # tuple is immutable, you can't change the things 

    print()

    print(len(things))


    mega = ([1,2,3], [4,5,6], [5,6,7], [5,6,7])
    print(mega)
    mega[0][1] = 66
    print(mega)
    print(mega[1])
    
    numbers1 = 1, 2, 3, 4
    numbers_list = list(numbers1)
    print(numbers1)
    print(numbers_list)

# take a look for method from python documentation and geeksforgeeks