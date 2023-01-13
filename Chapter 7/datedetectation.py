import re
data="31/04/2022"

dateDetection=re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
date=dateDetection.search(data)
if(int(date.group(1))>31 or int(date.group(1))<1):
    print("Invalid Date")
elif(int(date.group(2))>12 or int(date.group(2))<1):
    print("Invalid Date")
elif(int(date.group(3))>2999) or int(date.group(3))<1000:
    print("Invalid Date")
else:
    print("Valid Date")
dict={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
print("Day is: ",date.group(1))
print("Month is: ",dict[int(date.group(2))])
print("Year is: ",date.group(3))