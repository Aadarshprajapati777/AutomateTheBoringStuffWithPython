import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flip = []
    for i in range(100):
        flip.append(random.randint(0, 1))
        if flip[i] == 0:
            flip[i] = 'H'
        else:
            flip[i] = 'T'
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 0
    for i in range(99):
        
        if flip[i] == flip[i + 1]:
            count+=1
        else:
            count = 0
        if count == 6:
            numberOfStreaks += 1
            count = 0
            break
print(flip)
print(numberOfStreaks)

print('Chance of streak: %s%%' % (numberOfStreaks / 100))