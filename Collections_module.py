# Counter
from collections import Counter as counter
from collections import defaultdict as dd

a = "Tanvir Chowdhury"
b = counter(a)
print(b)
b.update("Sanaam teri kasaam")
print(b)
print(b['a'])
for i in b.elements():
    print(f"{i} : {b[i]}")

print(b.most_common(2))


# defaultDict
d = dd(lambda : 6644)
d['Tanvir'] = 6465
d['Mahi']
print(d['Mahi'])
print(d)
print(d.__missing__("Mahi"))

d1 = dd()
for i,j in [("Tanvir", 11744), ("Saquib", 11738)]:
    d1[i] = j

print(d1)


# orderedDict

    