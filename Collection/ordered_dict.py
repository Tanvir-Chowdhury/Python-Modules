from collections import OrderedDict as od

d = od()
d["a"] = 1
d["c"] = 3
d["b"] = 2

print(d)

d.move_to_end("c")
print(d)

d.move_to_end("b", last = False)
print(d)

d["c"] = 5
print(d)

print(d.pop("c"))
print(d)

print(d.popitem(last = False))
print(d)
