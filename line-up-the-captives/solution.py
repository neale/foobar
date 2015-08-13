import itertools
# Because at all times we have to find all the different permutations of the list
# This is perfect for dynamic programming. i.e. memoization

cache = []

def DP(rab, fn, *args):
    
    if rab not in cache:
        cache[rab] = fn(*args)
    return cache[rab]


def order(n, rab): 
    
    '''if there is only one rabbit then the tallest rabbit it placed at every
       different position in the line
       
       if there is exactly n rabbits to be seen then they line up ordered 
       with the tallest at the back/front
       
    '''
    if rab == 1: 
        f = reduce(lambda x,y:x*y,[1]+range(1,n))
        return f # all permutations
    
    elif rab == n:
        return 1 # only one order

    elif rab == (n - 1):
        return comb(n, 2) # the tallesy rabbit is second in line here
    
    return DP((n, rab), lambda: order(n - 1, rab - 1) + order(n - 1, rab) * (n - 1),)


''' fact(n rabbits, rabbits that can form a unique set):
    gives the maximum amount of ways you can sort the list /
    ways to arrange the rabbits (rab) in size (n) '''

def comb(n, rab): # for those who love VHDL 
    
    return len(list(itertools.product(xrange(n), repeat=rab)))


def answer(x, y, n):

    return str(order(n - 1, x + y - 2) * comb(x + y - 2, x - 1))


print answer(2, 2, 3)
print answer(1, 2, 6)
