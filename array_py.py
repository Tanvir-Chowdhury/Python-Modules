import array as arr

a = arr.array('i', [1, 2, 3])  # int
for i in range(0, 3):
    print(a[i], end=' ')
print()

b = arr.array('d', [1.5, 2.5, 3.2])  # float
for i in range(0, 3):
    print(b[i], end=' ')
print()

a.insert(1, 4)  # insert
for i in a:
    print(i, end=' ')
print()

b.append(5.6)  # append
for i in b:
    print(i, end=' ')
print()

print(a.index(4))  # index