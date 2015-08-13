import collections 
import itertools
def answer(meetings):
    
    sm = sorted(meetings, key = lambda pair: pair[0])
    print 'sorted: ', sm
    
    popped = []
    for i in range(0, len(sm)):
        if i+1 == len(sm):
            break
        else:
            if sm[i][1] <= sm[i+1][0]:
                popped.append(sm[i])
    print popped
    newlst = [items for items in sm if items not in popped]
    print newlst
    last = [x for x in range(0, len(newlst)-1) if newlst[x][1] <= newlst[x+1][0]]
    popped += last
    newlst = [items for items in last if items not in popped]
    print newlst
    
    print 'popped: ', popped

    return len(popped) if len(popped) > 0 else 1

print answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]])
print answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]])
