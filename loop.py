# while loop

i = 1
j = 10
while i<10 and j>=5:
    if j == 8:
        j=j-1
        continue
    if i == 4:
        break

    print(i,j)
    i=i+1
    j=j-1

# for loop 

numbers = [5,10,15,20,25]
sum = 0

for i in numbers:
    print(i, end = ' ')
    sum = sum + i

print(sum)

numbers = [1, 2, 3, 4 , 5, 6]

for i in range(6):
    print(numbers[i], end = ' ')

print()


text = 'pagla jhankar'

for ch in text:
    print(ch , end = ' ')

print()

for i in range(1, 10):       # 1 to 9
    print(i, end = ' ')

print()

for i in range (1, 10, 2):
    print(i, end = ' ')      # 1 to 9, after every 2 step

print()

numbers = [2,4,6,8,10]

for i in range(len(numbers)):
    print(i , ' ' , numbers[i])
