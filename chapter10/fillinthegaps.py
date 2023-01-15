import os,shutil,re
p=os.walk('/home/adarsh/Documents/AutomateThe BoringStuff/chapter10')
for folderName, subfolders, filenames in p:
    for filename in filenames:
        for filename in filenames:
            compileFile=re.compile(r'^spam')
            searchFilePrefix=compileFile.search(filename)
            
            