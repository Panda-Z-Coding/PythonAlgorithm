# 并查集
n = 10
fa = range(1, n + 1) #? 初始化父亲为自己
def find(x):
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

def merge(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        fa[fy] = fx


