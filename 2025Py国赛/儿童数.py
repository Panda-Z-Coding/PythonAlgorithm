import os
import sys
from collections import Counter
# ksm
MOD = 10**9 + 7

# 每个质数的个数
# 唯一分解定律

def f(n):
    factor = [] # 存质因数
    for nn in range(n, 0, -1):
        
        for i in range(2, nn + 1):
            while nn % i == 0:
                nn //= i
                factor.append(i)
            if nn == 1:
                break
    return factor

# a = 2024
# n = 1
# while a > 0:
#     n *= a
#     a -= 1

fa = f(2024)
cnt = Counter(fa)
# print(cnt) # 要过滤掉次数大于61的

# 2: 2017, 3: 1006, 5: 503, 7: 335, 11: 201, 13: 166, 17: 126, 19: 111, 23: 91, 29: 71, 31: 67
# 乘除是我可以选择(2 ^ 1 => 2 ^ 2017)的, 然后+1是因为我可以 2^0 
print((2017 // 61 + 1) * (1006 // 61 + 1) * (503 // 61 + 1) * (355 // 61 + 1) * (201 // 61 + 1)* (166 // 61 + 1) * (126 // 61 + 1) * (111 // 61 + 1) * (91 // 61 + 1) *  (71 // 61 + 1) * (67 // 61 + 1))
# print(17978112)


