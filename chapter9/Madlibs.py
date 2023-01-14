sentence="The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."
sentence=sentence.split()
for i in range(len(sentence)):  
    if sentence[i]=='ADJECTIVE':
        sentence[i]=input('Enter an adjective: ')
    if sentence[i]=='NOUN':
        sentence[i]=input('Enter a noun: ')
    if sentence[i]=='VERB.':
        sentence[i]=input('Enter a verb: ')

sentence=' '.join(sentence) 
print(sentence)