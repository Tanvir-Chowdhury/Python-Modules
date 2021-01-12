from collections import Counter

a = "sabbir"
c = Counter(a)
print(c)
print(c["b"])

print(issubclass(Counter, dict))

c.update("helloh")
print(c)

print()

e = Counter("Hello")
for i in "help":
    print(f'{i} : {e[i]}')

print(e.most_common(2))

e.clear
print(e)

print(c+e)
print(c-e)
print(e-c)
