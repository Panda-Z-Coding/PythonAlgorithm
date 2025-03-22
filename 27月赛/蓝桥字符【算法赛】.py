import os
import sys
from collections import Counter
s = sys.stdin.readline().strip()

c_l, c_la, c_lan = 0, 0, 0
for c in s:
    if c == 'l':
        c_l += 1
    elif c == 'a':
        c_la += c_l
    elif c == 'n':
        c_lan += c_la

print(c_lan)
