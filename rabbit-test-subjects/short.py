def answer(x, y):

    return int(100-(1/(sorted([x, y],key=sum).pop()/_))*100)

print answer([1.0], [1, 0])
print answer([2.299999999, 15.0, 102.400001, 3486.80000000002],
             [23.0, 150.0, 1024.0, 34868.0])


