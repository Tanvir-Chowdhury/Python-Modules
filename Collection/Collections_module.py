# Counter

from collections import Counter as counter
from collections import defaultdict as dd
from collections import OrderedDict as od
from collections import namedtuple as nt

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

o = od()
o["c"] = 3
o["a"] = 1
o["b"] = 2

print(o)
o.move_to_end("c")
print(o)

o.move_to_end("b", last = False)
print(o)

print(o.popitem())
print(o.popitem(last=False))

#NamedTuple

colors = nt("colors", "r g b")
red = colors(r = 255, g = 0, b = 255)
print(red.r)
print(red[0])
print(getattr(red, "r"))

print(red._asdict())

print(colors._make(["1","2","3"]))

print(colors(**{"r" : 255, "g" : 0, "b" : 0}))

print(red._fields)

print(red._replace(g = 3))
print(red)
