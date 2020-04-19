# Q 1.1
def count_stair_ways(n):
    if n == 1 or n == 0:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)


# Q 1.2
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    elif k == 0:
        return 0
    else:

        
        return count_k(n-k, k) + count_k(n, k-1)    



