import sys
import re,string

my_file = "running-config.cfg"

with open(my_file) as f:
    cfg_lines = f.read()
f.close()

new_file = re.sub(r" ip address 172\."," ip address 192.",cfg_lines)
with open(new_file,'w') as f:
    f.write(new_file)

f.close()
print (new_file)
