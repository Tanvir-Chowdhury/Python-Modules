from itertools import takewhile, tee, zip_longest, count, cycle, repeat
from itertools import dropwhile, groupby

for i in takewhile(lambda x:x<10, [1,2,3,10,11,12,4,15]):  # takewhile 
    print(i)

print()

for k in tee([1,2,3,4,5], 3): # tee
    for l in k:
        print(l)
    print()

for i in zip_longest("ZiP", "abcde", fillvalue="default"): # zip_longest
    print(i)

for i in count(5,5):  # count
    if i > 50 :
        break
    print(i)

c = 0
for i in cycle(["red", "green", "blue"]): # cycle
    if c > 10:
        break
    print(i)
    c += 1

for i in repeat("red", 5):  # repeat
    print(i)

for i in dropwhile(lambda x:x<7, [1,2,3,7,4]): # dropwhile
    print(i)

for i,j in groupby("AAAAABBBBBCCCCDDDAAAABAC"): # groupby
    print(f"{i} : {list(j)}")