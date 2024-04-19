""" i will update this in future :) """

# list list comprehension in python

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    odds = []                           # do this
    for num in numbers:
        if num%2 == 1 and num%3 != 0:
            odds.append(num)
    print(odds)

    odd_nums = [num for num in numbers]        # don't do this
    print(odd_nums)

    odd_nums = [num for num in numbers if num%2==1]
    print(odd_nums)
    
    odd_nums = [num for num in numbers if num%2==1 if num%3!=0]
    print(odd_nums)


    players = ['virat', 'rahul', 'rohit']
    ages = [37, 32, 38]

    player_age_comb = []

    for name in players:
        for age in ages:
            player_age_comb.append([name, age])

    print(player_age_comb)

def display_person(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


display_person(Name="Amir Khan", Age="45")