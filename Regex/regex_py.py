import re

text_to_speech = '''
Hello
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXY.Z

HA Ta Tanim Tanvir

12345678.900011210101.121231516123.3.
Bye
Mr. Tanvir
Mr Tanim
Mr Sifat
Mr. T
Mr S
tanvirvlogger@gmail.com
tanvirchowdhury6465@gmail.com
mp3-11744@yahoo.edu
'''

sentence = 'Hello, I am Tanvir, Bye'

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.(com|edu)')

matcher = pattern.finditer(text_to_speech)

#for match in matcher:
    #email = match.group(0)

with open('emails.txt', 'w') as f:
    for match in matcher:
        f.write(match.group(0)+'\n')

with open('phone_number.txt', 'r', encoding='utf-8') as f:
    p_numbers = f.read()

    pattern1 = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
    numbers = pattern1.finditer(p_numbers)

    for number in numbers:
        print(number)


    # There are few more regex fuctions : findall, match, search, (re.IGNORECASE / re.I)