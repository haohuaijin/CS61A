"""
The tree abstraction
A tree has a root label and a sequence of branches.
"""

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


#######################################
#                barrier              #
#######################################

"""
Partition trees
1. the left (index 0) branch contains all ways of partitioning n using at least one m,
2. the right (index 1) branch contains partitions using parts up to m-1, and
3. the root label is m.
"""

def partition_tree(n, m):
    """Retrun a partition tree og n using parts of up to m."""
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return tree(m, [left, right])


def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(label(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


def right_binarize(t):
    """Construct a right-branching binary tree."""
    return tree(label(t), binarize_branches(branches(t)))

def binarize_branches(bs):
    """Binarize a list of branches."""
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [right_binarize(first), binarize_branches(rest)]
    else:
        return [right_binarize(b) for b in bs]


#####################################################
##              Linked lists
#####################################################

empty = 'empty'
four = [1, [2, [3, [4, 'empty']]]]
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Retrun the first element of a linked list s."""
    assert is_link(s), 'first only applis to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements if a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

###########################################################
#                barrier
############################################################

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != 0:
        s = rest(s)
        length += 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list a."""
    while i > 0:
        s, i = rest(s), i-1
    return first(s)


# 递归实现
def len_link_recursive(s):
    """Retuen the length of a linked list s."""
    if s == empty:
        return 0
    return len_link_recursive(rest(s)) + 1

def getitem_link_recursive(s, i):
    """Return the element at index i of linked list s."""
    if i == 0:
        return first(s)
    return getitem_link_recursive(rest(s), i-1)

#########################################################3
def extend_link(s, t):
    """Return the list with the element of s followed by those of t."""
    assert is_link(s) and is_link(t), 's or t is not a link list'
    if s == empty:
        return t
    return link(first(s), extend_link(rest(s), t)) 


def apply_to_all_link(f, s):
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))


# my answer 
def keep_to_all_link_my(f, s):
    assert is_link(s), 's must is a link list'
    if s == empty:
        return s
    elif f(first(s)) == True:
        return link(first(s), keep_to_all_link_my(f, rest(s)))
    else:
        return keep_to_all_link_my(f, rest(s))

def keep_to_all_link_answer(f, s):
    assert is_link(s), 's must is a link list'
    if s == empty:
        return s
    else:
        kept = keep_to_all_link_answer(f, rest(s))
        if f(first(s)):
            return link(first(s), kept)
        else:
            kept


def join_link(s, separator):
    """Return a string of elements in s separated by seprator"""
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)



################################################3
# Partition
def partitions(n, m):
    """Return a linked list of partitions of n using parts of up to m.
    Eack partition is represented as a linked list.
    """
    if n == 0:
        return link(empty, empty)
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n-m, m)
        with_m = apply_to_all_link(lambda s: link(m, s), using_m)
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    string = apply_to_all_link(lambda s: join_link(s, " + "), lists)
    print(join_link(string, '\n'))













