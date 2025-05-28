def power(s):
    power_set = [[]]
    
    for data in s:
        for sub_data in power_set[:]:
            power_set.append(sub_data + [data])
    return power_set

input_set = [1,2,3]
print('Power set :', power(input_set))    