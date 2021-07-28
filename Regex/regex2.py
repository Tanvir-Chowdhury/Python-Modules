import re

# 1

'''namage = 
Tanvir is 19 and Sifat is 13
Ammu is 40 and Abbu is 60

ages = re.findall(r'\d{1,3}', namage)
names = re.findall(r'[A-Z][a-z]*', namage)

ageDict = {}
x = 0

for eachname in names:
    ageDict[eachname] = ages[x]
    x += 1

print(ageDict)'''

# 2

'''text = 'I will inform you about the information'
allinform = re.findall('inform',text)

for i in allinform:
    print(i)'''

# 3

'''text = 'I will inform you about the information'

for i in re.finditer("inform", text):
    print(i.group(), i.span())'''

# 4

'''str = 'sat,hat,mat,pat,cat,rat'
allat = re.findall(r'[shmp]at', str)

for i in allat:
    print(i)'''

# 5

'''food = 'rat sat mat hat'
regex = re.compile("[h]at")
food2 = regex.sub('food', food)
print(food2)'''

# 6

'''txt = 
My name is
Tanvir
Chowdhury

regex = re.compile("\n")
newtxt = regex.sub(" ", txt)
print(newtxt)'''

# 7

str = '123456 12345 1234 1213 1245698'
regex = re.findall("\d{5}", str)
for i in regex:
    print(i)