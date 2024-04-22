name1 = 'ayan banik'

name2 = "antar banik"

#for multiline string 
name3 = """arunima banik
arindam banik
anupoma banik"""

print(name1, name2) 
print(name3)


name = 'ayanbanik'
for ch in name:
    print(ch, end=' ')


# string is a sequence of character
print()
print(name[2])
print(name[-2])
print(name[1 : 6])
print(name[1:7:2])

# string is immutable
# immutable means changeable

rename = 'ayanbanik'
# rename[0] = 'g'       # can't do that
print(rename)

if 'banik' in rename:
    print('exists')
# rename = rename.upper()
renameUpper = rename.upper()
print(renameUpper)


# take a look for method from python documentation and geeksforgeeks