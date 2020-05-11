#### part 1
# Q 1.1
def height(t):
    """Return the height of a tree

    >>> t = tree(3, [tree(5,[tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        return max([height(bran) for bran in branches(t)]) + 1



# Q 1.2
def square_tree(t):
    """
    Return a tree with the square of every element in t
    """
    square = label(t)*label(t)
    if is_leaf(t):
        return tree(square)
    else:
        return tree(square, [square_tree(bran) for bran in branches(t)])



# Q 1.3
## 看看答案，感觉自己做的不过优雅
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [x]
    elif not is_leaf(tree):
        path = [find_path(bran,x) for bran in branches(tree) if find_path(bran,x) != None]
        if len(path) >= 1:
            return sum([[label(tree)]]+path, [])



# Q 1.4
"""
1. 1 not
2. 1, yes label(t)
3. 2, no
4. 2, yes label(branches(t)[0])
5. yes, yes is_lead(branches(t)[1])
6. [2,3], no
7. 1, yes branches(tree(2, [t, []]))[0]
"""


##### part 2
# Q 2.1
"""
>>> lst1 = [1, 2, 3]
>>> lst2 = lst1
>>> lst1 is lst2
>>> lst2.extend([5, 6])
>>> lst1[4]
>>> lst1.append([-1, 0, 1])
>>> -1 in lst1
>>> lst2[5]
>>> lst3 = lst2[:]
>>> lst3.insert(3, lst2.pop(3))
>>> len(lst1)
>>> lst1[4] is lst3[6]
>>> lst3[lst2[4][1]]
>>> lst1[:3] is lst2[:3]
>>> lst1[:3] == lst2[:3]
>>> x = (1, 2, [4, 5, 6])
>>> x[2] = [3, 5, 6]
>>> x
>>> x[2][0] = 3
>>> x

"""



# Q 2.2 
## 审好题
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    count = 0
    for element in lst:
        if element == x:
            count += 1
    while count > 0:
        lst.append(el)
        count -= 1


# Q 2.3
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    res = {}
    for element in s:
        key = fn(element)
        if key in res:
            res[key] += [element]
        else:
            res[key] = [element]
    return res




#### Options
# Q 1 partition_options
def partition_options(total, biggest):
    """
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """
    if total == 0:
        return [[]] #注意这里的判断条件
    elif total < 0 or biggest == 0:
        return []
    else:
        with_biggest = partition_options(total-biggest, biggest)
        without_biggest = partition_options(total, biggest-1)
        with_biggest = [[biggest] + element for element in with_biggest]
        return with_biggest + without_biggest


## Q 2 min_elements
def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    
























































############################################################
##                       tree ADT
############################################################
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