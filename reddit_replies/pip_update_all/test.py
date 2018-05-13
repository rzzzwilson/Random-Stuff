#Updates all the packages from pip list
 
#Subprocess allows for system calls, re allows for text replacement
import subprocess,re
 
#Gets the results from the system call 'pip list' representing the installed packages and makes it into a list of said packages
packageList=subprocess.run(['pip','list'],stdout=subprocess.PIPE).stdout.decode('utf-8')
packageList = packageList.split('\n')[2:-1]

#packages=[re.sub(r'\s+.+','',package).lower() for package in packageList.split('\n')[2:-1]]
packages = [x.split()[0] for x in packageList]
 
#Makes a system call to update each of those packages with 'pip install -U <package>', except for pip itself having a special call of 'python.exe -m pip install -U pip'
for package in packages:
    print(package)
#    if(package=='pip'): subprocess.run(['python.exe','-m','pip','install','-U','pip'])
#    else: subprocess.run(['pip','install','-U',package])
