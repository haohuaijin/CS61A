#####################################
############* OOP####################
#####################################

#* 1.1
class Student:
    students = 0 # this is a class attribute
    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, 'students.')
        ta.add_students(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}
    
    def add_students(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


"""
>>> snape = Professor("Snape")
>>> harry = Student("Harry", snape)
* There are now 1 students.

>>> harry.visit_office_hours(snape)
* Thanks snape

>>> harry.visit_office_hours(Professor("Hagrid"))
* Thanks Hagrid

>>> harry.understanding
* 2

>>> [name for name in snape.students]
* [Harry]

>>> x = Student("Hermione", Professor("McGonagall")).name
! There are now 2 stuents

>>> x
* Hermione

>>> [name for name in snape.students]
* [Harry]
"""


#* 1.2
class Email:
    """Every email object has 3 instance sttributes: the
    message, the sender name, and the recipient name"""
    def __init__(self, msg, sender_name, recipient_name):
        self.message = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance atttibute clients, which 
    is a dictionary that associates client names with
    cline objects."""
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        if not self.clients.get(email.recipient_name, 0):
            return "Error"
        self.clients[email.recipient_name].receive(email)
        

    def register_client(self,client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute"""
        self.clients[client_name] = client
     

class Client:
    """Every Client has instance attrubutes name (which is
    used for adderssing emails to the client), server(which
    is used to send emails out to other clients), and
    inbox(a list of all emails the client has recived).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server
        server.register_client(self,self.name)#! 注意这里

    def compose(self, msg, recipient_name):
        """Send an email with the given massage msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        self.inbox += [email]



##################################*
######*     Inheritance ###########
##################################*

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + " says woof!")

#* 2.1 
class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')
    
    def lose_life(self):
        if self.is_alive and self.lives != 0:
            self.lives -= 1
        else:
            self.is_alive = False
            print("The " + self.name + " has no more lives to lose.")

#* 2.2
class NoisyCat(Cat):
    def talk(self):
        print(self.name + ' says meow!')
        print(self.name + ' says meow!')


#* 2.3 
class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x-1)

class B(A):
    def f(self):
        return 4

"""
>>> x, y = A(), B()
>>> x.f()
#* 2

>>> B.f()
#* 4 
#! ERROR request i argument self 

>>> x.g(x, 1)
#* 4

>>> y.g(x, 2)
#* 8
"""


#####################################*
#######*     Linked lists ###########*
#####################################*

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

#* 3.1
def sum_nums(lnk):
    """ 
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    total = 0
    while lnk is not Link.empty:
        total += lnk.first
        lnk = lnk.rest
    return total



#* 3.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    #! 待优化
    note = Link(0)
    res = note
    while True:
        first = 1
        for i in range(len(lst_of_lnks)):
            first *= lst_of_lnks[i].first
            lst_of_lnks[i] = lst_of_lnks[i].rest
        note.rest = Link(first)
        note = note.rest
        for i in range(len(lst_of_lnks)):
            if not isinstance(lst_of_lnks[i], Link):
                return res.rest
    return res.rest


    
#* 3.3
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link != Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest


def filter_no_iter(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> list(filter_no_iter(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    if link == Link.empty:
        return
    elif f(link.first):
        yield link.first
    yield from filter_no_iter(link.rest, f)


##################################*
#* Midterm Teview Snax
def feed(snax, x, y):
    """
    >>> feed([1, 1, 1], 2, 2) # The two robots both refill once at the beginning
    2
    >>> feed([1, 2, 2], 2, 2) # Only one robot refills to feed the middle student
    3
    >>> feed([1, 1, 1, 2, 2], 2, 2)
    4
    >>> feed([3, 2, 1, 3, 2, 1, 1, 2, 3], 3, 3)
    6
    """
    """
    i, j = 0, len(snax)-1
    le, ri = x, y
    res = 2
    while j > i:
        le, i = le-snax[i], i+1
        if le <= 0:
            le, res = le+x, res+1

        print(le)
        if sum(snax[i:j+1]) <= le or sum(snax[i:j]) <= ri:
            return res

        ri, j = ri-snax[j], j-1
        if sum(snax[i:j+1]) <= le or sum(snax[i:j]) <= ri:
            return res
        print("ri = {}".format(ri))
        if ri <= 0:
            ri, res = ri+y, res+1
    return res
    """









