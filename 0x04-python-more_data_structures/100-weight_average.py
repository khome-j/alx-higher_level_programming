#!/usr/bin/python3

def weight_average(my_list=[]):
    div = 0
    count = 0
    sum = 0

    for i in range(len(my_list)):
        count = my_list[i][0] * my_list[i][1]
        sum += count
        div += my_list[i][1]

    sum /= div
    return(sum)
