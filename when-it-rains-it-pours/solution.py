#!/usr/bin/env python

def answer(heights):

    left_pointer, right_pointer = 0, 0 #left, right
    last_max = 0 #number in puddle
    standing_water = 0 #number at top
    hutch = 0 #puddle
    area = 0 #volume
    #run_off = xvolume
    for block in heights: 
        if block >= right_pointer:
            right_pointer = block
            standing_water = last_max
            run_off = 0 #xvolume
        if left_pointer > right_pointer: #
            last_max += 1
            hutch += left_pointer - block
            run_off += left_pointer - block
        else: # 
            area += hutch
            run_off = 0
            left_pointer = right_pointer
            right_pointer = 0
            hutch = 0
            last_max = 0
            standing_water = 0

    else:
        if left_pointer > right_pointer:
            hutch -= standing_water * (left_pointer - right_pointer)
            area += hutch - run_off
    return area

print answer([10, 5, 2, 5, 1, 2, 10])
