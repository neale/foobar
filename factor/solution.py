def answer(n):
    
    factor = 1
    while n % 4 < 1:
        n //= 4
        factor *= 2
    root = int(n**.5)
    lst = range(int(2*(root**.5)+1))
    foo = [[first*factor,second*factor,third*factor,last*factor] for last in lst for third in lst for second in lst for first in[root, root - 1]if (first**2)+(second**2)+(third**2)+(last**2)
    == n]
    res = len(list(filter((lambda x: x > 0), foo[0])))
    return res 
