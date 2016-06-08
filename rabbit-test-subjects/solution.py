def answer(x, y):;q

    # create a sorted list of the sums of x and y
    sums = sorted([sum(x), sum(y)])

    # find the percentage of change
    change  = sums[0] / sums[1]
    percent = int(100 - change * 100)

    return percent
