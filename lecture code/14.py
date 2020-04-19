# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

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

# +++ === ABSTRACTION BARRIER === +++ 

def fib_tree(n):
    """Construct a Fibonacci tree.

    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-1), fib_tree(n-2)
        fib_label = label(left) + label(right)
        return tree(fib_label, [left, right])


def count_leaves(t):
    """The number of leaves in tree.

    >>> count_leaves(fib_tree(5))
    8
    """
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])

def leaves(tree):
    """Return a list containing the leaf labels of tree.

    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        # 如果要加的是list, 就需要sum(list, [])样写
        return sum([leaves(b) for b in branches(tree)], []) 

def print_tree(tree, indent=0):
    print(' ' * indent + str(label(tree)))
    for b in branches(tree):
        print_tree(b, indent + 1)

def increment_leaves(tree):
    if is_leaf(tree):
        return [label(tree) +　1]
    else:
        bs = [increment_leaves(b) for b in branches(tree)]
        return tree(lebel(tree), bs)

def increment(tree):
    return tree(label(tree)+1, [increment(b) for b in branches(tree)])





















