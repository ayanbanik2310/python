# key value pair
# object
# hash table
# {key:value,  key:value,  key:value}


if __name__ == '__main__':
    numbers = [12, 56, 98, 78, 56, 12, 26 , 98]
    person1 = ['ayan' , 'anter', 'anupoma', 'arindam', 'arunima']

    person = {
                'name': 'ayan',
                'age': 23, 
                'address' : 'habiganj',
                'job' : 'student'
            }
    print(person)
    print(person['name'], person['job'])
    print(person.keys())
    print(person.values())

    person['language'] = 'python'
    print(person)

    person['name'] = 'antar'
    print(person)

    print()
    for key, value in person.items():
        print(key, value)


    # list , with index
    number = [12, 56, 98, 78, 56, 12, 26 , 98]
    for i, num in enumerate(number):
        print(i, num)