# used the skeleton from https://gist.github.com/igor47/7228586
def answer(levels):
    lefties = [(levels[0],0)]
    volume = 0

    for level in levels[1:]:
        print type(level)
        lefties = [(lelft_level, distance+1) for lelft_level, distance in lefties]
        mini = lefties[-1][0]
        maxi = lefties[0][0]
        if level < mini:
            lefties.append((level,0))
        elif level == mini:
            lefties[-1] = (level,0)
        elif level > mini:
            # lets count how much water would be hold back
            
            ### try here ###
            #where [space][0] = left_level, [space][1] = distance
            '''            
            for space in lefties[::-1]:
                pointer = space[0]
                distance = space[1]
                volume += (min(level, pointer) - mini) * (distance-1)
                if pointer > level:
                    lefties.append((pointer, distance))
                    break
                mini = pointer
            lefties = [(length, distance) for length, distance in lefties if length >= level]
           # if True:
            lefties.append((level, 0))
            '''
            ### end here ###
            while len(lefties) > 0:
                left_level,distance = lefties.pop()
                print 'left_level:', left_level
                print 'dist:', distance
                volume += (min(level,left_level) - mini) * (distance-1)
                if left_level > level:
                    lefties.append((left_level,distance))
                    break
                mini = left_level
            lefties = [(l,distance) for l,d in lefties if l >= level]
            if True:
                lefties.append((level,0))       

    return volume

testcases = [
    ([1,0,1], 1),
    ([5,0,5], 5),
    ([5,0,4], 4),
    ([4,0,5], 4),
    ([4,0,5,0,2], 6),
    ([0,1,0,1,0], 1),
    ([
    ([0,1,0,0,1,0], 2),
    ([4,2,2,1,1,1,3], 8),
    ([0,3,2,1,4], 3),
    ([1,0,1,0], 1),
    ([1,0,1,2,0,2], 3),
    ([2,5,1,2,3,4,7,7,6], 10),
    ([5,1,0,1],1),                 # thanks https://news.ycombinator.com/item?id=6640085
    ([2,5,1,2,3,4,7,7,6,3,5], 12), # thanks https://news.ycombinator.com/item?id=6640105
    ([3,0,1,0,2], 5),
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

