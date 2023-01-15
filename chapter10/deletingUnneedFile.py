import shutil, os
p=os.walk('/home/adarsh/Documents')
for folderName, subfolders, filenames in p:
    for filename in filenames:
        checkFileSize=os.path.getsize(os.path.join(folderName,filename))
        if checkFileSize > 102400:
            print(filename,"is greater than 100MB")