#! /usr/bin/env python2
import collections
import itertools
"""
def ordered_permutations(list1, list2):
    perms = []
    if len(list1) + len(list2) == 1:
        yield [list1 or list2]
    if list1:
        for item in ordered_permutations(list1[1:], list2):
            #perms.append([list1[0]] + item)
            a = [list1[0]]+item
            yield(a)
    if list2:
        for item in ordered_permutations(list1, list2[1:]):
            #perms.append([list2[0]] + item)
            a = ([list2[0]]+item)
            yield(a)
    #return perms

"""
def interleave(L1, L2, answer=None):
    if answer is None:
        answer = '';
        if not L1 and not L2:
            print answer
        else:
            if L1:
                a = answer + L1[0]
                interleave(L1[1:], L2, a)
                if L2:
                    ans = answer + L2[0]
                    interleave(L1, L2[1:], ans)

def answer(seq):
    # get root node
    root = seq[0]
    count = 0
    a, b, = '', ''
    for i in seq:
        if i > root:
            a = a+str(i)
        elif i < root:
            b = b+str(i)
    #lseq = str(str(i) for i in seq if i > root)
    #sseq = str([str(i) for i in seq if i < root])
    print a, b
    # get purmutions
    # permutations = list(itertools.permutations(seq[1:], len(seq)-1))
    #permutations = ordered_permutations(lseq, sseq)
    interleave(a, b)
    return 
#    lst = []
#    for perm in permutations:
#        lst.append(perm)
    lst = []
    return len(lst)

if __name__ == '__main__':

    sequences = [[5, 9, 8, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    for seq in sequences:
        print "number of sequences: ", answer(seq), '\n'

