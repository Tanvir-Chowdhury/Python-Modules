import os

print(os.access("ordered_dict.py", os.X_OK))
print(os.access("ordered_dict.py", os.F_OK))
print(os.access("ordered_dict.py", os.W_OK))
print(os.access("ordered_dict.py", os.R_OK))

print(os.getcwd())

print(os.popen("cp text1 text2"))  #we can os.system also

