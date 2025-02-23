
 #? a对b向上取整
a=5
b=2
print(a // b) # 2
print((a + b - 1) // b) # 3
print((a-1) // b + 1)

#! 1. 整除
# a整除b，记为a|b => b % a == 0
#? 性质：
'''
如果a|b, b|c => a|c
如果c|a, c|b => c|(na + mb)
'''

#! 2. 同余
#? 设整数m不为零， 且 m|(a-b) ，则a同余于b mod m，也就是a和b都mod m 的结果相同
# 记为 a = b(mod m)
# 性质：
# 自反，对称，传递
#! 可以在+ 和 * 的运算中对于每个数字都求余数，这和对于最终答案求余是一样的
# 只要在运算中不出现除法，那么都可以分解成每一步的求余

#! 3. GCD => 最大公因数
#? a > b; 被除数和除数的最大公因数等于除数和余数的最大公因数
#? gcd(a, b) = gcd(b, a % b) 
def gcd_(a, b):
    #! 辗转相除法
    if b == 0:
        return a
    return gcd_(b, a % b)

print(gcd_(18, 12)) # 6

#? 也可以从math中import
from math import gcd
print(gcd(64, 120))

#! 4. LCM => 最小公倍数
#? gcd(a. b)*lcm(a, b) = ab
#? => lcm(a, b) = ab // gcd(a, b)

def lcm(a, b):
    # Least Common Multiple
    return a * b // gcd_(a, b)

print(lcm(4, 6)) # 12

