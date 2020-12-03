import os

os.chdir("/home/codinxter/Desktop/Temp_texts/")

file_path = os.listdir()

for f in file_path:

    f_name, f_ext = os.path.splitext(f)
    f_title, f_num = f_name.split("-")
    
    new_name = f"{f_num.strip()[1:].zfill(2)}-{f_title.strip()}{f_ext.strip()}"

    os.rename(f, new_name)