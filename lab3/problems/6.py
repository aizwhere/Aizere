

def find_common_elements(firstList, secondList):
    answer = []
    for x in firstList:
        for y in secondList:
            if x == y:
                answer.append(x)
    return answer            
firstList = [1, "one", 1.0]
secondList = [2.0, "one", 1]
k = find_common_elements(firstList, secondList)
print(k)