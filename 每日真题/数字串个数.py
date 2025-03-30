import os
import sys

mod = int(1e9 + 7)

# 长度10000的数字字符串


def ksm(a, b, c):
    ans = 1
    a %= c
    while b > 0:
        if b & 1:
            ans = ans * a % c
        a = a * a % c
        b >>= 1
    return ans


# 我们可以先计算出总的数量，之后慢慢减去不符合条件的个数
# 总的满足没有0的数量是 9 ^ 10000
# 没有3的个数 8 ^ 10000 没有 7 的个数 8 ^ 10000
# 没有3没有7的 7 ^ 10000 
print((ksm(9, 10000, mod) - ksm(8, 10000, mod) * 2 + ksm(7, 10000, mod)) % mod)

# 没有3和没有7的情况在我们计算单独没有3或者7到时候已经包含
# 所以要加回来


