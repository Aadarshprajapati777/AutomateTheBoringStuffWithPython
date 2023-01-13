import re 

def removeChar():
    line=input("enter a string: ")
    char=input("enter a char you want to remove: ")
    if (char == ''):
        print("Error: please enter some char to remove" )
    delchar=re.compile(char)
    deletingchar=delchar.search(line)
    if deletingchar== None:
        print("the char you want to remove is not in the string")
    else:
        newString=delchar.sub('',line)
        print("the string without the char is: ", newString)
    
removeChar()