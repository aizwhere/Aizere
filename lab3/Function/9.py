def calculate_running_average(list): 
    sum = 0 
    for i in range(1,len(list)+1): 
        utn = list[i-1] 
        list[i-1]=float(f"{(sum+list[i-1])/i:0.2f}") 
        sum += utn 
    return list 
list = [1,2,3,4,5,6,7,8,9,10] 
k = calculate_running_average(list) 
print(k)