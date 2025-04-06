import os
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(range(1, n + 1))
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = sum(int(x) for x in str(i))

# print(b)
# lambda 函数魅力时刻
a.sort(key = lambda x:(b[x], x))
# print(*a)
print(a[m - 1])


