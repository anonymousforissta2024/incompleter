#Source: https://stackoverflow.com/questions/31354629/python-list-loop-error-typeerror-list-indices-must-be-integers-not-str
#Inventory and the Loot value
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#Function to loop through the items in the list
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for j, k in inventory.items():
        print(str(k) + ' ' + j)
        item_total += k
    print('Total number of items: %s' % str(item_total))

#Where the problem occur
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if addedItems[i] in inventory.keys():
            #Edit: I see an error here now, but I will fix it after I get the loop working
            inventory[addedItems[i]] + 1
        else:
            inventory.setdefault(addedItems[i], 1)

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)