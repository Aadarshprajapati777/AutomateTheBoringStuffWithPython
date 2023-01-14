file = open('/home/adarsh/Documents/AutomateThe BoringStuff/chapter9/somefile.txt','a')
file.write('\nthis is the second line')
file.close()

file=open('/home/adarsh/Documents/AutomateThe BoringStuff/chapter9/somefile.txt')
filecontent=file.read()
file.close()
print(filecontent)