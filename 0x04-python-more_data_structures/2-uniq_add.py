#!/usr/bin/python3

def uniq_add(my_list=[]):
    count = []
    sum = 0
    for item in range(len(my_list)):
        if my_list[item] in count:
            continue
        else:
            count.append(my_list[item])
            sum += my_list[item]
    return(sum)
