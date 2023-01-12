import re
data='batman is playing chess with batwoman'
searchBat=re.compile(r' bat(man|woman)')
searching=searchBat.search(data)
print(searching.group())
