import pyinputplus as pyip
print("enter bread type: ",end='')
bread=pyip.inputMenu(['wheat', 'white',  'sourdough'],prompt='what type of bread do you like?\n',numbered=True)
protien=pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],prompt='which type of protien do you want?\n', numbered=True)
cheese=pyip.inputYesNo(prompt='do you want extra cheese?\n')
if(cheese.lower()=='yes'):
    cheeseType=pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
choice=pyip.inputYesNo(prompt='do you want mayo, mustard, lettuce, or tomato\n')
noOfSandwich=pyip.inputInt(prompt='how many sandwich do you want?\n', min=1)