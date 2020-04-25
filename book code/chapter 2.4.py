""" 
# 好玩的
from unicodedata import lookup

suits = ['heart', 'diamond', 'spade', 'club']

string = [lookup('WHITE ' + s.upper() + ' SUIT') for s in suits]

for i in string:
    print(i)
"""















