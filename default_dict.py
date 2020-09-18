from collections import defaultdict as dd

def defaluValue():
    return 6465

normal_dict = dd(defaluValue)
normal_dict["a"] = 66
normal_dict["b"] = 44
normal_dict["c"] = 77
normal_dict["d"]

print(normal_dict)

other_dict = dd(lambda : 11744)
other_dict["Mahi"] = 6644
other_dict["Tanvir"] 
print(other_dict)

a = [("a", (1,2)), ("b", 2), ("c", 3)]
b = dd(list)
for i,j in a:
    b[i].append(j)
print(b)
print(b.get("a"))

name = "sabbir"
mydict = dd(int)
for i in name:
    mydict[i] += 1
print(mydict)

