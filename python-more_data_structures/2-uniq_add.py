#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_nums = []
    total = 0
    for i in my_list:
        if i not in uniq_nums:
            uniq_nums.append(i)
            total = total + i
    return total
