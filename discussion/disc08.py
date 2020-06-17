##################################
######*  Effciency ###############
##################################*

#* 1.1
def bonk(n):
    total = 0
    while n >= 2:
        total += n:
        n = n / 2
    return total
#? answer: logarithmic


#* 1.2
def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
#? answer: linear


#* 1.3
def mod_7(n):
    if n % 7 == 0:
        return 0
    else:
        return 1 + mod_7(n-1)
#? answer: logarithmic
#! Constant, since at worst it will require 6 recursive calls to reach the base case.

































