thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")#any iterable object (tuples, sets, dictionaries etc.)
thislist.extend(thistuple)#Add elements of a tuple to a list:
print(thislist)

'''
['apple', 'banana', 'cherry', 'kiwi', 'orange']
'''