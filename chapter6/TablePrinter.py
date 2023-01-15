tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


for i in range(len(tableData[1])):
    for j in range(len(tableData)):
        print(tableData[j][i],end='')
    print()
    