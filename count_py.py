import itertools
from itertools import count
from itertools import cycle

for i in count(1):
    if i > 500:
        break
    print(i)\

c = 1
for i in cycle([' ','red', 'green', 'blue']):
    if c > 100:
        break
    print(i)
    c += 1