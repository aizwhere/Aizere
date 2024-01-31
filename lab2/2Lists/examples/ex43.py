fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
#Return the item if it is not banana, if it is banana return orange
print(newlist)

'''
['apple', 'orange', 'cherry', 'kiwi', 'mango']
'''