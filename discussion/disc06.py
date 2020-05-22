###################
#* 1. Nonlocal
##################

#* 1.2
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def helper(f):
        nonlocal n
        n = f(n)
        return n
    return helper


#* 1.3
#TODO
def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """    
    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = 
        def get(i):
            if i == 0:
                return value
            return 
        
    return prepend, get



######################33
#* Iterators
#######################

#*2.1
"""
>>> lst = [6, 1, "a"]
>>> next(lst)
Error

>>> lst_iter = iter(lst)
>>> next(lst_iter)
6

>>> next(lst_iter)
1

>>> next(iter(lst))
6

>>> [x for x in lst_iter]
["a"]
"""


###########################
#*   Generators
###########################
#* 2.1
def merge(a,b):
    """
    >>> def sequence(start, step):
    ...     while True:
    ...         yield start
    ...         start += step
    >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
    >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
    >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
    >>> [next(result) for _ in range(10)]
    [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
    """
    fir, sec = next(a), next(b)
    while True:
        if fir < sec:
            yield fir
            fir = next(a)
        elif fir > sec:
            yield sec
            sec = next(b)
        else:
            yield fir
            fir, sec = next(a), next(b)


#* 2.2 
def generate_subsets():
    """
    >>> subsets = generate_subsets()
    >>> for _ in range(3):
    ...     print(next(subsets))
    ...
    [[]]
    [[], [1]]
    [[], [1], [2], [1, 2]]
    """
    res, index = [[]], 0
    yield res
    while True:
        index += 1
        for i in range(len(res)):
            res.append(res[i] + [index])
        yield res



#! 2.3 一开始没做出来，看了答案
def sum_paths_gen(t):
    """
    >>> t1 = tree(5)
    >>> next(sum_paths_gen(t1))
    5
    >>> t2 = tree(1, [tree(2, [tree(3), tree(4)]), tree(9)])
    >>> sorted(sum_paths_gen(t2))
    [6, 7, 10]
    """
    if is_leaf(t):
        yield label(t)
    for bran in branches(t):
        for i in sum_paths_gen(bran):
            yield label(t) + i


#* Trie Recursion
def collect_words(t):
    """Return a list of all the words contained in the tree where the value of each node in
    the tree is an individual letter. Words terminate at the leaf of a tree.

    >>> greetings = tree('h', [tree('i'),tree('e', [tree('l', [tree('l', [tree('o')])]), tree('y')])])
    >>> collect_words(greetings)
    ['hi', 'hello', 'hey']
    """
    if is_leaf(t):
        return [label(t)]
    words = []
    for bran in branches(t):
        words += [label(t) +i  for i in sum_paths_gen(bran)]
    return words


















##########################################################################3
################! tree #################################################3
##########################################################################

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])