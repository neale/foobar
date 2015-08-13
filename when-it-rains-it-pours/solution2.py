def twitter_puddle(seq):
    """scan seq from left to right
       there can be more that one puddle
    """
    print seq
    left = right = 0
    last_max = 0 # number of contributionsin puddle
    number_at_top = 0  # number of contributions @ last high on the right
    puddle = 0    # volume in current puddle
    volume = 0   # volume after last high on the right
    xvolume = 0  # volume after last high on the right - splills off for last puddle
    for s in seq:
        if s >= right:
            right = s
            number_at_top = last_max
            xvolume = 0
        if left > right:
            last_max += 1
            print "number in puddle", last_max
            puddle += (left - s)
            xvolume += (left - s)
        else: # puddle if full - right >= left -> next puddle
            volume += puddle
            print 'area', volume
            xvolume = 0
            left = right
            right = 0
            puddle = last_max = number_at_top = 0
    else:
        # last puddle - extra volume has to be subtracted
        # right is lower than left, so puddle volume has to be corrected
        assert left > right
        puddle -= number_at_top * (left - right)
        volume += puddle - xvolume
       
    return volume

#print twitter_puddle([1, 4, 2, 5, 1, 2, 3])
print twitter_puddle([10, 5, 2, 5, 1, 2, 10])
#print twitter_puddle([1, 2, 4, 10, 1, 9, 3])
#print twitter_puddle([10, 1, 10, 1, 10, 1, 10, 1])
#print twitter_puddle([1, 1, 1, 1, 1, 1, 1])
#print twitter_puddle([9, 8, 7, 6, 5, 4, 3, 2, 1])
#print twitter_puddle([1, 2, 3, 4, 5, 6, 7])
#print twitter_puddle([1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1])
