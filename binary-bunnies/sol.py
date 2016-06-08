from math import factorial as fact

class Tree:

    def __init__(self, *seq):
        self.root = None
        self.right = None
        self.left = None
        self.count = 0
        for val in seq:
            self.add(val);

    def add(self, val):
        if self.root is None:
            self.root = val

        if val < self.root:
            if self.left is not None:
                self.left.add(val)
            else:
                self.left = Tree(val)

        elif val > self.root:
            if self.right is not None:
                self.right.add(val)
            else:
                self.right = Tree(val)

def nodes(node):

    if node is None:
        return 0

    if node is not None:
        return 1 + nodes(node.left) + nodes(node.right)

def permutations(node):

    if node is None:
        return 1

    leftnodes  = nodes(node.left)
    rightnodes = nodes(node.right)
    leftperms  = permutations(node.left)
    rightperms = permutations(node.right)

    perms = leftperms * rightperms
    return choosek(leftnodes + rightnodes, rightnodes) * perms

def choosek(n, k):

    return fact(n) / (fact(k) * fact(n - k))

def answer(seq):
    tree = Tree(*seq)
    print str(permutations(tree))

if __name__ == '__main__':

    sequences = [[5, 9, 8, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    for seq in sequences:
        print "number of sequences: ", answer(seq), '\n'
