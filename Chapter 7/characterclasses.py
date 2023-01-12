import re
data='12 bat, 10 ball, 15 football, 100 chess, 99 badminton'
characterClass=re.compile(r'\d+\s\w+')
searching= characterClass.findall(data)
print(searching)
