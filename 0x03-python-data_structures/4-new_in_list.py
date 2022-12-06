#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    modified_list = my_list.copy()

    if (idx < 0) or (idx > len(my_list) - 1):
        return(None)
    modified_list[idx] = element
    return(modified_list)
