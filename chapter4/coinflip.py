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
    for i in range(94):
        if flip[i] == flip[i + 1] == flip[i + 2] == flip[i + 3] == flip[i + 4] == flip[i + 5]:
            numberOfStreaks += 1
            break
print(flip)

print('Chance of streak: %s%%' % (numberOfStreaks / 100))