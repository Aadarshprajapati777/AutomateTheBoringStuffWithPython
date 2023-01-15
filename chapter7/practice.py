import re;
data= 'my num is 123-123-345 and bishal num is 234-234-432'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
match= phoneNumRegex.search('my num is 123-123-345')
print("number found: ",match.group())
