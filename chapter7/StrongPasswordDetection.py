import re
password="Masswordadaa123"
if len(password)<8:
    print("please enter a password with 8 atleast characters")
else:
    passwordSearching=re.compile(r'[A-Z]+[a-z]+[0-9]+')
    searching=passwordSearching.search(password)
    if searching==None:
        print("please enter a strong password")
    else:
        print("password is strong")