# 包括！1->n-1 的所有整数即可

# 但是我们不能破坏原来数组的顺序，因为是
# 要相邻的元素做差的绝对值

# 先把所有的差求出来，放到一个数组
# 然后sort，然后和[1->n-1] 一一对比
# 如果有不一样的就不是
import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
n = a[0]
a.pop(0)
c = []
for i in range(1, len(a)):
    c.append(abs(a[i] - a[i-1]))
c.sort()
b = [i for i in range(1, n)]
# 比较
##print(b)
##print(c)
for i in range(n-1):
    if b[i] != c[i]:
        print("Not jolly")
        exit(0)
print("Jolly")
