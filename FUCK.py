import os,platform
os.system('clear')
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    os.system('chmod +x FILE;./FILE')
elif bit=='32bit':
    os.system('chmod +x FILE;./FILE')
