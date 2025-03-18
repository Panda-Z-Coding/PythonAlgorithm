import sys

def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])  # 路径压缩,因为这个在后续查找的时候会自动全部指向一个祖先根
    return fa[x]

'''
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def merge(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        fa[fy] = fx
'''

def merge(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        fa[fy] = fx  # 按祖先合并
#? >=> 
# 读取输入
m, n = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
fa = [i for i in range(m * n + 1)]  # 初始化并查集

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    merge(a, b)
# print(*fa)
# 计算独立的集合数量
roots = set()
for i in range(1, m * n + 1):
    # print(find(i))
    roots.add(find(i))
# print(roots)
print(len(roots))
