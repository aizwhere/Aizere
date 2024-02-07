def find_common_elements(list1, list2):
    common_elements = [num for num in list1 if num in list2]
    return common_elements

list1 = [1, 2, 3, 4, 5]
list2 = [2, 4, 3, 10, 7]
result = find_common_elements(list1, list2)
print(result) 