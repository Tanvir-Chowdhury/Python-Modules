from collections import namedtuple as nt

colors = nt("colors", "red green blue")

red = colors(red = 255, green = 0, blue = 255)
red1 = colors(255,0,255)
print(red1)
print(red)
print(red.red)
print(getattr(red, "red"))
print(red._asdict())
print(red._make([1,2,3]))
b = colors(**{'red':255,'green':0,'blue':0})
print(b)

pets = nt("pets", ["name", "age"])
cat = pets("Tanvir", 18)
print(cat)
print(cat.name)
print(getattr(cat, "name"))
print(cat._asdict())

print(red._fields)

print(red._replace(green=1))