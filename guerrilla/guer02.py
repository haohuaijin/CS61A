###########################**
#*###### 1. Mutability #######
############################*
#* 1.1
"""
1. Name two data types that are mutable. What does it mean to be mutable?
!Dictionaries, Lists. Being mutable means we can modify them after they’ve been
!created..
"""

#* 1.2
"""
2. Name at least two data types at are not mutable.
!Tuples, functions, int, float
"""

#* 1.3 
"""
the first don't error.
the second error. because the key of dictrary must't mutable. Don't hash
"""

#* 1.4
"""
>>> a = [1, [2, 3], 4]
>>> c = a[1]
>>> c
[2, 3]

>>> a.append(c)
>>> a
[1, [2, 3], 4, [2, 3]]

>>> c[0] = 0
>>> c
[0, 3]

>>> a
[1, [0, 3], 4, [0, 3]]

>>> a.extned(c)
>>> c[1] = 9
>>> a
![1, [0, 9], 4, [0, 9], [0, 3]] False
![1, [0, 9], 4, [0, 9], 0, 3] True

>>> list1 = [1, 2, 3]
>>> list2 = [1, 2, 3]
>>> list2 == list1
True
>>> list1 is list2 
False
"""


#* 1.5

""" #!
1 What is the difference between the append function, extend function, and the
’+’ operator?
The append and extend functions both return a value of none. They just mutate the
list that we are currently working on. For example, if we did a = [1,2,3].append(4),
a would evaluate to None because the return value of the append function is None.
However, when we are using the + operator, we return the value of the two lists
added together. If we did a = [1,2,3] + [4,5,6], we would get that a is equal to
[1,2,3,4,5,6]. The difference between appends and extends is that appends opens
up one single space in the list to place the the parameter of appends. This allows
for appends to take in both numbers and lists. The extends function takes in a list
(that we will refer to as a) as its parameter and will open len(a) number of boxes
in the original list that we are extending.

"""
#* 2.
"""
>>> a = [1, 2, [3, 4], 5]
>>> b = a[:]
>>> b[1] = 6
>>> b[2][0] = 7

>>> b
[1, 6, [7, 4], 5]
>>> a
[1, 2, [7, 4], 5]

!A,B are not the same. Because lists are mutable, when you assign b to a shallow
!copy of a, you are also copying the pointers to lists within a. Thus, that is why
!nested elements inside a list changed in both arrays, but all the other elements were
!unaffected by changes to the shallow copy.
"""


##########################################*
############*  Data Abstraction###########*
##########################################*
#* 2.1
"""
construction: build a Data type
deconstruction: fetch a feature of a Data type
"""

#* 2.2
"""
the simplify is broken the barrier.
if the implement is use two element list,it is work.
if is not two element list, it is error.
"""

#* 2.3
"""
1. if wo don't use the construction and deconstruction to 
get the feature and build a data type in a function.
answer: 
Put simply, a Data Abstraction Violation is when you bypass the constructors and
selectors for an ADT, and directly use how its implemented in the rest of your code,
thus assuming that its implementation will not change.
We cannot assume we know how the ADT is constructed except by using constructors and likewise, we cannot assume we know how to access details of our ADT
except through selectors. The details are supposed to be abstracted away by the
constructors and selectors. If we bypass the constructors and selectors and access
the details directly, any small change to the implementation of our ADT could break
our entire program

2. because the Data Abstraction, we can use the data type to 
do many things, and we don't need to know the implement. 
answer:
With a correct implementation of these data types, it makes for more readable code
because:
-You can make constructors and selectors have more informative names.
-Makes collaboration easier
-Other programmers don’t have to worry about implementation details.
-Prevents error propagation.
-Fix errors in a single function rather than all over your program.
"""



################################################*
#############* Tree#############################
###############################################*
#* 3.1
def tree(label, branches = []):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [label] + list(branches)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

#* 3.2
def is_min_heap(t):
    for bran in branches(t):
        if (label(bran) < label(t)) or (not is_min_heap(bran)):
            return False
    return True


#* 3.3
def largest_product_path(tree):
    """
    >>> largest_product_path(None)
    0
    >>> largest_product_path(tree(3))
    3
    >>> t = tree(3, [tree(7, [tree(2)]), tree(8, [tree(1)]), tree(4)])
    >>> largest_product_path(t)
    42
    """
    if not tree:
        return 0
    if is_leaf(tree):
        return label(tree)
    max_bran = max([largest_product_path(bran) for bran in branches(tree)])
    return max_bran * label(tree)


#* 3.4
#todo
def max_tree(t):
    """
    >>> max_tree(tree(1, [tree(5, [tree(7)]),tree(3,[tree(9),tree(4)]),tree(6)]))
    tree(9, [tree(7, [tree(7)]),tree(9,[tree(9),tree(4)]),tree(6)])
    """
    if is_leaf(t):
        return tree(label(t))
    else:
        new_branches = [max_tree(b) for b in branches(t)]
        new_label = max([label(t)]+[label(bran) for bran in new_branches])
        return tree(new_label, new_branches)
    
#* 3.5
def level_order(tree):
    res = [label(tree)]
    stack = [bran for bran in branches(tree)]
    while len(stack) > 0:
        t = stack.pop(0)
        res.extend([label(t)])
        if not is_leaf(t):
            stack.extend([bran for bran in branches(t)])
    return res


#* 3.6 
def all_paths(t):
    if is_leaf(t):
        return [[label(t)]]
    else:
        res = []
        for bran in branches(t):
            for i in all_paths(bran):
                res.append([label(t)] + i)
        return res



######################################################*
###############* Nonlocal ############################
######################################################*
#* 4.1
"""
perter parker the greatest superhero
"""

#* 4.2
"""
! 方程属于True 
! a = lambda x: x
!>>> if (not 3) or x:
!>>>   print('hello')
!hello
"""


#* 4.3
def make_max_finder():
    """
    >>> m = make_max_finder()
    >>> m([5, 6, 7])
    7
    >>> m([1, 2, 3])
    7
    >>> m([9])
    9
    >>> m2 = make_max_finder()
    >>> m2([1])
    1
    """
    max_element = 0
    def helper(t):
        nonlocal max_element
        if max(t) > max_element:
            max_element = max(t)
        return max_element
    return helper



#* 4.4
x = 5
def f(x):
    def g(s):
        def h(h):
            nonlocal x
            x = x + h
            return x
        nonlocal x
        x = x + x
        return h
    #print(x) # 7
    return g
t = f(7)(8)(9)

"""
a. What is t after the code is executed?
23 
b. In the h frame, which x is being referenced? Which frame?
!f frame
c. In the g frame, is a new variable x being created?
no
"""



######################################*
##########* Iterators and Generators ##
#######################################*

#* 5.1
"""
iterable: can use iter() to become the iterator
iterator: use next() to get next element
generaotr: use yield return a iterator
answer:
An iterable is any object that can be passed to the built-in iter function. In other
words, an iterable is any object that can produce iterators.
An iterator is an object that provides sequential access to values one by one. Its
contents can be accessed through the built-in next function, and it will signal there
are no more values available with a StopIteration exception when next is called.
A generator object is an iterator, but it is created in a special way – generator
functions are defined as a function that yields its values instead of returning them.
When generator functions are called, they return a generator object, which can then
be used as an iterator.
"""

#* 5.2
"""
>>> new_list = [2, 3, 6, 8, 8, 3]
>>> next(new_list)
error

>>> iter(new_list)[1]
error

>>> [x for x in iter(new_list)]
!error我做错了
[2, 3, 6, 8, 8, 3]

>>> for i in range(len(iter(new_list))):
...     new_list.append(2)
!error list_iterator not len function
"""


#* 5.3
#a. 
def infinity1(start):
    while True:
        start = start + 1
        return start
#b. 
def infinity2(start):
    while True:
        start = start + 1
        yield start
"""
What would python display?
>>> infinity1
function
>>> infinity2
function
>>> infinity1(2)
3
>>> infinity2(2)
genetor
>>> x = infinity1(2)
>>> next(x)
error
>>> y = infinity2(2)
>>> next(y)
3
>>> next(y)
4
>>> next(infinity2(2))
3
"""


#* 5.4
def generate_constant(x):
    """A generator function that repeats the same value x forever.
    >>> area = generate_constant(51)
    >>> next(area)
    51
    >>> next(area)
    51
    >>> sum([next(area) for _ in range(100)])
    5100
    """
    while True:
        yield x


#* 5.5
def black_hole(seq, trap):
    """A generator that yields items in SEQ until one of them matches TRAP, in which case that
    value should be repeatedly yielded forever.
    >>> trapped = black_hole([1, 2, 3], 2)
    >>> [next(trapped) for _ in range(6)]
    [1, 2, 2, 2, 2, 2]
    >>> list(black_hole(range(5), 7))
    [0, 1, 2, 3, 4]
    """
    for ele in seq:
        if trap == ele:
            while True:
                yield trap
        yield ele



#* 5.6 
"""
>>> def weird_gen(x):
...     if x % 2 == 0:
...         yield x * 2
>>> wg = weird_gen(2)
>>> next(wg)
>>> next(weird_gen(2))
#! 4 true 44 
>>> next(wg)
end 

>>> def greeter(x):
...     while x % 2 != 0:
...         print('hi')
...         yield x #!返回生成器
...         print('bye')
>>> greeter(5)
#! <Generator Object> 

>>> gen = greeter(5)
>>> g = next(gen)
hi


>>> g = (g, next(gen))
>>> g
byehi(5, 5)

>>> next(gen)
byehi5

>>> next(g)
error

#! An iterator ______________________ a generator
#! A generator is a(n) ______________________ iterator
An iterator is not always represented by a generatorA generator is a(n) a
special type of/user defined iterator
"""


#* 5.7
def gen_inf(lst):
    """
    >>> t = gen_inf([3, 4, 5])
    >>> next(t)
    3
    >>> next(t)
    4
    >>> next(t)
    5
    >>> next(t)
    3
    >>> next(t)
    4   
    """
    while True:
        yield from lst



#* 5.8
def naturals():
    i = 1
    while True:
        yield i
        i += 1

def filter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter(range(5), is_even))
    [0 , 2 , 4]
    >>> all_odd = (2*y-1 for y in range (5))
    >>> list(filter(all_odd, is_even))
    []
    >>> s = filter(naturals(), is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for ele in iterable:
        if fn(ele):
            yield ele




#* 5.9
"""
What could you use a generator for that you could 
not use a standard iterator paired with a function for?
#todo maybe i should use element one by one and don't save.
answer:
#! Call next on an infinite iterator
"""


#* 5.10
def tree_sequence(t):
    """
    >>> t = tree(1, [tree(2, [tree(5)]), tree(3, [tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield label(t)
    for bran in branches(t):
        yield from list(tree_sequence(bran))


#* 5.11
def make_digit_getter(n):
    """ Returns a function that returns the next digit in n
    each time it is called, and the total value of all the integers
    once all the digits have been returned.
    >>> year = 8102
    >>> get_year_digit = make_digit_getter(year)
    >>> for _ in range(4):
    ...     print(get_year_digit())
    2
    0
    1
    8
    >>> get_year_digit()
    11
    """
    total = 0
    def helper():
        nonlocal n, total
        if n > 0:
            x, n = n % 10, n // 10
            total += x
            return x
        return total
    return helper

#get_year_digit = make_digit_getter(8102)
#for _ in range(5):
#     print(get_year_digit())



#* 5.12
def iter(iterable):
    def iterator(msg):
        nonlocal iterable
        if msg == 'next':
            next = iterable[0]
            iterable = iterable[1:]
            return next
        elif msg == 'stop':
            raise StopIteration
    return iterator

def next(iterator):
    return iterator('next')

def stop(iterator):
    iterator('stop')

lst = [1, 2, 3]
iterator = iter(lst)
elem = next(iterator)


