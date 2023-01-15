import pathlib,os,shutil
for folderName, subfolders, filenames in os.walk('/home/adarsh/Documents/AutomateThe BoringStuff'):
    for filename in filenames:
        if filename.endswith('.txt'):
            shutil.copy(os.path.join(folderName,filename) ,'/home/adarsh/Documents/AutomateThe BoringStuff/Chapter10')
            print(filename,"copied sucessfully")