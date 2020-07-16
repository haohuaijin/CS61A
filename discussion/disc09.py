class VendingMachine:
    k = 0
    def __init__(self, k, v):
        self.soda = JunkDrink(self)
        self.k = k
        if v:
            print(isinstance(self.soda.machine, VendingMachine))

class JunkDrink:
    def __init__(self, machine):
        self.machine = machine

a = VendingMachine(1, False)
b = VendingMachine.__init__(a, 2, False) #__init__就是一个函数
VendingMachine.__init__(VendingMachine, 10, False)


"""
>>> a.k
!2
>>> b.k
!Error
>>> VendingMachine.k
*10
>>> isinstance(b, VendingMachine)
!False
>>> a is a.soda.machine
*True
>>> VendingMachine is a.soda.machine
!False
>>> c = VendingMachine
>>> c.__init__(c, 11, True)
!False
>>> c.soda.machine is VendingMachine
!True
>>> a.k == c.k
*False
>>> c.soda.machine.k
!11
"""



















