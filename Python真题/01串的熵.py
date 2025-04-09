import os
import sys
import math
# from Decimal import decimal
n = 23333333
di = 11625907.5798
di = int(di * 10000)
for i in range(1, n):
    cur = -(i * (i / n) * math.log2(i / n)) -((n-i)*((n-i)/n)*math.log2((n-i)/n)) 
    cur = int(cur * 10000)
    if cur == di:
        print(i)
        break

# print(-(1 * (1 / 3) * math.log2(1 / 3)))
