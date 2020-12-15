import os

'''print(os.access("ordered_dict.py", os.X_OK))
print(os.access("ordered_dict.py", os.F_OK))
print(os.access("ordered_dict.py", os.W_OK))
print(os.access("ordered_dict.py", os.R_OK))

print(os.getcwd())

print(os.popen("cp text1 text2"))  #we can os.system also

print(os.listdir())

print(os.path.isdir('/home/usr/local/bin/pipenv'))'''

db_user = os.environ.get("DB_USER")
db_pass = os.environ.get("DB_PASS")

print(db_user)
print(db_pass)