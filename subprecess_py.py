import subprocess

p1 = subprocess.run("ls", shell = True, capture_output= True, text = True) # run commands on shell

print(p1.stdout) # It shows the output of p1 | without decode() it prints in byte

print(p1.returncode) # shows the errors
