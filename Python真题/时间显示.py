import os
import sys
input = sys.stdin.readline
from datetime import *

n = int(input().strip())

delta = timedelta(milliseconds = n)
s = datetime(1970, 1, 1, 0, 0, 0)

e = s + delta
# print(e)
ans = e.strftime('%H:%M:%S')

print(ans)
