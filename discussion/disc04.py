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
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return sum([count_k(n-i, k) for i in range(1,k+1)])    
 



# Q 2.1
"""
>>> a = [1, 5, 4, [2, 3], 3]
>>> print(a[0], a[-1])
1 3
>>> len(a)
5
>>> 2 in a
False
>>> 4 in a
True
>>> a[3][0]
2
"""


# Q 2.2
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [i * s[i] for i in range(len(s)) if i % 2 == 0]



# Q 2.3 
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) < 1:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        # 认真思考什么要由最大值
        first = s[0] * max(max_product(s[2:]), max_product(s[3:]))
        second = s[1] * max(max_product(s[3:]), max_product(s[4:]))
        return max(first, second)



# Whole Numbers
# 1. hole number
def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    if n % 1000 // 100 > n % 100 // 10:
        return check_hole_number(n // 100)
    return n < 10

# 2. mountain number
def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    def helper(m, flag):
                



    return helper(n, (n % 10) > (n % 100 // 10))




