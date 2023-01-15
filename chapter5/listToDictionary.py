# inventory.py
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL THIS PART IN
        print(v,k)
        item_total+=v
    print("Total number of items: " + str(item_total))



def addToInventory(inventory, addedItems):
    for k,v in inventory.items():
        for i in addedItems:
            if k == i:
                inventory[k]+=1
          
    return inventory
                


inventory= {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inventory, dragonLoot)
displayInventory(inv)