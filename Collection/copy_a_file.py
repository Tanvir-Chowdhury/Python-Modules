import subprocess
import shutil

status = subprocess.call("cp text1 text2" , shell = True)  #We can also do that with subprecoess.check_output 

if status != 0:
    if status < 0:
        print(f'killed by signal {status} ')
else:
    print("succesfully exicuted command")


print(shutil.copyfile("text1", "text2"))  # we can also do that with shutil.copy2, shutil.copyfileobj, shutil.copy

