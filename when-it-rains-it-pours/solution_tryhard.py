
def answer(heights):
    area = 0
    '''iterate through hutches left to right, storing local maxes and comparing them
       store the height and index in a tuple
       find the distence between maxes, and fill to min(two local maxes)'''

    left_pointer = [(heights[0], 0)]
    for hutch in heights[1:]:
        left_pointer = [(left_hutch, space+1) for left_hutch, space in left_pointer]
        end_max = left_pointer[0][0]
        end_min = left_pointer[-1][0]

        if hutch < end_min:
            left_pointer.append((hutch, 0))
        elif hutch == end_min:
            left_pointer[-1] = (hutch, 0)
        elif hutch > end_min:

            '''make a single pass through the loop, computing the area of the 
            rain that would 
            fall between the local maxes'''

            for space in left_pointer[::-1]:
                pointer = space[0]
                distance = space[1]
                area += (min(hutch, pointer) - end_min) * (distance-1)
                if pointer > hutch:
                    left_pointer.append((pointer, distance))
                    break
                end_min = pointer
            '''at the end of the loop'''

            left_pointer = [(s, d) for s, d in left_pointer if s >= hutch]
            left_pointer.append((hutch, 0))

    return area

testcases = [
        ([1,0,1], 1),
        ([1, 2, 3, 2, 1], 0),
        ([1, 4, 2, 5, 1, 2, 3], 5),
        ([5,0,5], 5),
        ([5,0,4], 4),
        ([4,0,5], 4),
        ([4,0,5,0,2], 6),
        ([0,1,0,1,0], 1),
        ([0,1,0,0,1,0], 2),
        ([4,2,2,1,1,1,3], 8),
        ([0,3,2,1,4], 3),
        ([1,0,1,0], 1),
        ([1,0,1,2,0,2], 3),
        ([2, 5, 1, 2, 3, 4, 7, 7, 6], 10),
        ([5, 1, 0, 1], 1),
        ([2, 5, 1, 2, 3, 4, 7, 7, 6, 3, 5], 12),
        ([3,0,1,0,2], 5),
        ([1, 1, 1, 1, 1], 0),
        ([5, 1, 5, 1, 5], 8),
        ([5, 1, 5, 1, 5, 1], 8)
        ]
try:
    from nose.tools import eq_
    def test_water():
        for case in testcases:
            yield check, case[0], case[1]

    def check(levels, volume):
        res = water(levels)
        eq_(volume, res, "%r fills %d not %d" % (levels, volume, res))
except ImportError:
    pass

if __name__ == "__main__":
    for case in testcases:
        w = answer(case[0])
        if w == case[1]:
            print "TRUE: %s holds %s" % (case[0], w)
    else:
        print "MISMATCH: %s holds %s (got %s)" % (case[0], case[1], w)

