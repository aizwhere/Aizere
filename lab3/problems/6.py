firstList = [1, "one", 1.000, 2]
secondList = [2.0, "one", 1]

def find_common_elements(firstList, secondList):
    newList = []
    for element in firstList:
        if element in secondList:
            newList.append(element)
    return newList
 

answer = find_common_elements(firstList, secondList)
print(answer)