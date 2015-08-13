def answer(heights):
    area = 0
    '''iterate through hutches left to right, storing local maxes and comparing them
       store the height and index in a tuple
       find the distence between maxes, and fill to min(two local maxes)'''

    left_pointer = list((heights[0], 0)) 
    for hutch in heights:
        
        left_pointer = [(left_hutch, space+1) for left_hutch, space in left_pointer]
        end_max = left_pointer[0][0]
        end_min = left_pointer[-1][0]
        
        if hutch < end_min:
            left_pointer.append((hutch, 0))
        elif hutch == end_min:
            left_pointer[-1] = (hutch, 0)
        elif hutch > end_min:
        
    '''make a single pass through the loop, computing the area of the rain that would 
       fall between the local maxes'''
        
            for space in lefties[::-1]:
                pointer = space[0]
                print 'pointer', pointer
                distance = space[1]
                print 'dist:', distance
                area += (min(hutch, pointer) - end_min) * (distance-1)
                if pointer > hutch:
                    lefties.append((pointer, distance))
                    break
                end_min = pointer
    '''at the end of the loop 
    '''
            left_pointer = [(s, d) for s, d in left_pointer if l >= hutch]
            lefties.append((level, 0))
 
        return volume
