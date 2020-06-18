################################
########*  Linked lists #######
###############################*

#* 1.1
"""
What is a linked list? Why do we consider it a naturally recursive structure?
a linked list is a struct, that has a first and a rest, and the rest is also
a link list. the first is a element, it can be a int, string, or a link.
"""

#* 1.2
"""
Link(
    'C', 
    Link(
        Link(
            6,
            Link('a'))
        Link('s')))
"""

#* 1.3
def has_cycle(link):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    """
    """ don't suit the porblem
    head = link
    while link != Link.empty:
        if link.rest == head:
            return True
        link = link.rest
    return False
    """
    #* sol 1 用了一种搜索方法
    tortoise = link
    hare = link.rest
    while tortoise.rest and hare.rest and hare.rest.rest:
        if tortoise is hare:
            return True
        tortoise = tortoise.rest
        hare = hare.rest.rest
    return False
    #* sol 2
    seem = []
    while link.rest:
        if link in seen:
            return True
        seen.append(link)
        link = link.rest
    return False

#* 1.4 
def seq_in_link(link, sub_link):
    """
    >>> lnk1 = Link(1, Link(2, Link(3, Link(4))))
    >>> lnk2 = Link(1, Link(3))
    >>> lnk3 = Link(4, Link(3, Link(2, Link(1))))
    >>> seq_in_link(lnk1, lnk2)
    True
    >>> seq_in_link(lnk1, lnk3)
    False
    """
    while link != Link.empty and sub_link != Link.empty:
        if link.first == sub_link.first:
            sub_link = sub_link.rest
        link = link.rest
    if sub_link == Link.empty:
        return True
    return False
    #! 可以用递归


########################################*
##########*  OOP #######################
########################################*

#! 这里看答案
#* 2.1
"""
What is the relationship between a class and an ADT?
the class is alse a ADT, and class just like a blackbox,
it has some value and method, wo can use it, but don't need
to know how it implenent.
"""

#* 2.2
"""
What is the definition of a Class, What is the definition of an Instance?
The definition of Class is the thing use the key word Class, and it can
has value and class. 
the definition of Instance is a specific class, we use *Instance = class() *
to definition, and it can use method in class.
"""

#* 2.3
"""
What is a Class Attribute? What is an Instance Attribute?
Class Attribute is the value all Instance of the class have same value.
Instance Attribute is the value that every is different.
"""

#* 2.4
class Foo():
    x = 'bam'
    def __init__(self, x):
        self.x = x
    def baz(self):
        return self.x

class Bar(Foo):
    x = 'boom'
    def __init__(self, x):
        Foo.__init__(self, 'er' + x)
    def baz(self):
        return Bar.x + Foo.baz(self)

"""
>>> foo = Foo('boo')
>>> Foo.x
'bam'

>>> foo.x
'boo'

>>> foo.baz()
'boo'

>>> Foo.baz()
#! error required one argument

>>> Foo.baz(foo)
'boo'

>>> bar = Bar('ang')
>>> Bar.x
'boom'

>>> bar.x
'erang'

>>> bar.baz()
'boomerang'
"""


#* 2.5 
class Student:
    def __init__(self, subjects):
        self.current_units = 16
        self.subjects_to_take = subjects
        self.subjects_learned = {}
        self.partner = None
    
    def learn(self, subject, units):
        print("I just learned about " + subject)
        self.subjects_learned[subject] = units
        self.current_units -= units

    def make_friends(self):
        if len(self.subjects_to_take) > 3:
            print('Whoa! I need more help!')
            self.partner = Student(self.subjects_to_take[1:])
        else:
            print("I'm on my own now!")
            self.partner = None
    
    def take_course(self):
        course = self.subjects_to_take.pop()
        self.learn(course, 4)
        if self.partner:
            print('I need to switch this up!')
            self.partner = self.partner.partner
            if not self.partner:
                print("I have failed to make a friend :(")

"""
>>> tim = Student(['Chem1A', 'Bio1B', 'CS61A', 'CS70', 'CogSci1'])
>>> tim.make_friends()
Whoa! I need more help!

>>> print(tim.subjects_to_take)
['Chem1A', 'Bio1B', 'CS61A', 'CS70', 'CogSci1']

>>> tim.partner.make_friends()
Whoa! I need more help!

>>> tim.take_course()
I just learned about chem1A #! CogSci1
I need to switch this up!

>>> tim.partner.take_course()
I just learned about Bio1B #! Cogsci1
#! 下面是错误的，多加上了
#I need to switch this up!
#I have failed to make a friend :(

>>> tim.take_course()
I just learned about  #! CS70
! I need to switch this up!
! I have failed to make a friend :(

>>> tim.make_friends()
I'm on my own now
"""


#* 2.6
"""
>>>cat = Cat('Tuna')
>>>kitten = kitten('Fish', cat)
>>>cat.meow()
meow, Tuna is hungry
>>>kitten.meow()
i'm baby, Fish is hungry
I want mama Tuna
>>>cat.eat()
meow
>>>cat.meow()
meow, my name is Tuna
>>>kitten.eat()
i'm baby
>>>kitten.meow()
meow, my name is Fish
I want mama Tuna
"""

class Cat():
    noise = 'meow'
    def __init__(self, name):
        self.name = name
        self.hungry = True

    def meow(self):
        if self.hungry:
            print("{}, {} is hungry".format(self.noise, self.name))
        else:
            print("{}, my name is {}".format(self.noise, self.name))

    def eat(self):
        print(self.noise)
        self.hungry = False

class Kitten(Cat):
    noise = "i'm baby"
    def __init__(self, name, mother):
        Cat.__init__(self, name)
        self.mother = mother
    
    def meow(self):
        Cat.meow(self)
        print("I want mama {}".format(self.mother.name))























###################################*
###########* Class #################
###################################*
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'















