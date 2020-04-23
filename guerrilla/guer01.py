# Q 1.1
"""
>>> lst = [1,2,3,4,5]
>>> lst[1:3]
[2,3]

>>> lst[0:len(lst)]
[1,2,3,4,5]

>>> lst[-4:]
[2,3,4,5]

>>> lst[3:]
[4,5]

>>> lst[1:4:2]
[2,4]

>>> lst[:4:2]
[1,4]

>>> lst[1::2]
[2,4]

>>> lst[::-1]
[5,4,3,2.1]

>>> lst + 100
error

>>> lst3 = [[1], [2], [3]]
>>> lst + lst3
[1,2,3,4,5,[1],[2],[3]]
"""


# Q 1.2
# 画图略过

# Q 1.3
def map_mut(f, L):
    """
    >>> L = [1, 2, 3, 4]
    >>> map_mut(lambda x: x**2, L)
    >>> L
    [1, 4, 9, 16]
    """
    for i in range(0,len(L)):
        L[i] = f(L[i])

# Q 1.4
"""
# 1.4.1
if you use 
l = [1,2,3]
s = l
this is copying a pointer

if you use
l = [1,2,3]
s = l.copy()
this is a new list

# 1.4.2
use list.copy()
"""



# Q 1.5 
#??? 有疑问
"""
1. Base Case(s)
2. Way(s) to reduce the problem into a smaller problem of the same type.
3. Recursive case(s) that uses the solution of the smaller probelm to solve the original(large) problem.
"""

# Q 1.6
# When you define a function, Python does evaluate the body of the function


# Q 1.7
# 识别递归三要素


# Q 1.8
# 画图


# Q 1.9
def cascade(n):
    print(n)
    if n >= 10:
        cascade(n // 10)
        print(n)
"""
>>> cascade(4)
123
12
1
12
123
"""


# Q 1.10
def paths(m, n):
    """
    >>> paths(2,2)
    2
    >>> paths(117, 1)
    1
    """
    """
    def helper(i, j):
        right, up = 0, 0
        if i < m - 1:
            up = helper(i+1, j)
        else:
            return 1
        if j < n - 1:
            right = helper(i, j+1)
        else:
            return 1
        return right + up
    return helper(0, 0)
    """
    # good answer
    if m == 1 or n == 1:
        return 1
    return paths(m-1, n) + paths(m, n-1)


# Q 1.11
def merge(s1, s2):
    """ Merge two sorted lists
    >>> merge([1,3], [2,4])
    [1,2,3,4]
    >>> merge([1,2],[])
    [1,2]
    """
    """
    def helper(a, b, res):
        if len(a) < 1:
            return res + b
        if len(b) < 1:
            return res + a
        
        if a[0] <= b[0]:
            res += [a[0]]
            a = a[1:]
        else:
            res += [b[0]]
            b = b[1:]
        return helper(a, b, res)
    return helper(s1, s2, [])
    """
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])


# Q 1.12
def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a dash.
    >>> mario_number('-P-P-') # jump, jump
    1
    >>> mario_number('-P-P--') # jump, jump, step
    1
    >>> mario_number('--P-P-') # step, jump, jump
    1
    >>> mario_number('---P-P-') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number('-P-PP-') # Mario cannot jump two plants
    0
    >>> mario_number('----') # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('----P----')
    9
    >>> mario_number('---P----P-P---P--P-P----P-----P-')
    180
    """
    """
    if len(level) <= 1:
        return 1

    f, s, t = 0, 0, 0
    if level[:3] == "-P-":
        f = mario_number(level[2:])
    if level[:3] == "---":
        s = mario_number(level[2:])
    if level[:2] == "--":
        t = mario_number(level[1:])

    return f + s + t
    """
    def ways(n):
        if n == len(level) - 1:
            return 1
        if n >= len(level) or level[n] == 'P':
            return 0
        return ways(n+1) + ways(n+2)
    return ways(0)





















