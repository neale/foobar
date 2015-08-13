def answer(x):
    # your code heredef answer(x):
    return balanced_ternary(ternary_num(x))
 
def ternary_num(x):
    res = ""
    while x > 0:
        res = str(x % 3) + res
        x /= 3
    return int(res) 
 
def balanced_ternary(t):
     #convert to ternary
    res = map(int, str(t))[::-1] # iterating the digit from right --> left
    for i in range(0, len(res)):
        # zeros will remain zeros and ones remain ones
        # the only thing we need to convert is 2 into +- (== +1-1)
        if res[i] == 2:
            res[i] = -1
            res = inc(res, i + 1)
 
    # convert from (1,0,-1) representation to (R,-,L)
    return ['-' if x == 0 else ('R' if x == 1 else 'L') for x in res]
 
 
def inc(arr, ind):
    """
    calculate the carryover
    """
    if len(arr) == ind:
        arr += [1] # prepend the last carryover
    elif arr[ind] == -1:
        arr[ind] = 0
    elif arr[ind] == 0:   
        arr[ind] = 1
    elif arr[ind] == 1: 
        arr[ind] = -1
        arr = inc(arr, ind + 1)
    else: # arr[ind] == 2
        arr[ind] = 0
        arr = inc(arr, ind + 1)
    return arr

print answer(8)
