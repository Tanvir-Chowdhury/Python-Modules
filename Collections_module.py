from collections import Counter as counter
a = "Tanvir Chowdhury"
b = counter(a)
print(b)
b.update("Sanaam teri kasaam")
print(b)
print(b['a'])
for i in b.elements():
    print(f"{i} : {b[i]}")

print(b.most_common(2))
