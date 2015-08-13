def answer(heights):
    
    lmax, rmax = 0, 0
    left_pointer = 0
    right_pointer = len(heights) - 1
    area = 0

    ''' traverse the list from both sides, looking for maximums
        once maximums are found on both sides, the unfilled area 
        between them is calculated. By the time that the pointers 
        meet in the middle, the area of the water will be found'''

    while left_pointer < right_pointer:

        lheight = heights[left_pointer] #eliminates constant lookups
        rheight = heights[right_pointer]
        if lmax < lheight:
            lmax = lheight
        if rmax < rheight:
            rmax = rheight
        if rmax >= lmax:
            area += lmax - lheight
            left_pointer += 1
        else:
            area += rmax - rheight
            right_pointer -= 1
    return area
print answer([1, 4, 2, 5, 1, 2, 3])
 max_left = 0
max_right = 0
left = 0
right = len(heights) - 1
volume = 0
while left < right:
if max_left < heights[left]:
max_left = heights[left]
if max_right < heights[right]:
max_right = heights[right]
if max_right >= max_left:
volume += max_left - heights[left]
left += 1
else:
volume += max_right - heights[right]
right -= 1
return volume

