import os
import pathlib
p=os.path('/home/adarsh/Documents/AutomateThe BoringStuff')
for files in p.glob('*.txt'):
   readfile=open(files)
print(readfile.read())