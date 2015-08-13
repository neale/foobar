def recurs(n, guazes, squares):
    if n == 0:
        return guazes
    for i in range(len(squares)):
        if n >= squares[i]:
            return min(recurs(n - squares[i], guazes + 1, squares[i:]),
                       recurs(n, guazes, squares[i + 1:]))
    return guazes

def answer(n):
    squares = map(lambda x: x ** 2, xrange(1, int(n ** 0.5 + 1)))[::-1]
    return recurs(n, 0, squares)


print answer(24) #  3
print answer(160) # 2
print answer(128)
