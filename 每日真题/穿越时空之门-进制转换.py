import os
import sys

# 十进制转换四进制

# def tran(n, base = 4):
#     res = []
#     while n > 0:
#         res.append(n % base)
#         n //= base
#     return res
# ans = 0
# for i in range(1, 2024 + 1):
#     bi = tran(i, 2)
#     fo = tran(i)
#     if sum(bi) == sum(fo):
#         ans += 1
# print(ans)



def tran(n, base = 10):
    # 就是一直取模添加, 整除等于
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    while n > 0:
        n, rem = divmod(n, base)
        res.append(digits[rem])

    return res[::-1]

print(*tran(3, 2), sep='')

# def tran(n, base = 10):
#     digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     res = []
#     while n > 0:
#         n, rem = divmod(n, base)
#         res.append(digits[rem])
#     return res[::-1]
