def word_frequency(s): 
    empty_dict = {} 
    for x in s: 
        empty_dict.update({x : s.count(x)}) 
    return empty_dict

s = input()
result = word_frequency(s)
print(result)