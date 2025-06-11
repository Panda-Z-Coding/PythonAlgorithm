def dfs(x, fu):
    # 当前节点和父节点
    global ans 
    for y, w in t[x]:
        if y == fu:
            continue
        dfs(y, x)
        if dp1[y] + w > dp1[x]:
            # 先存次长
            dp2[x] = dp1[x]
            # 再更新最长
            dp1[x] = dp1[y] + w
        elif dp1[y] + w > dp2[x]: # dp2[x] < dp1[y] + w < dp1[x]
            # y出发的最长没有大过x的最长但是又比x的次长大, 就要更新x的次长
            # 注意这里使用的是 ~ elif ~
            dp2[x] = dp1[y] + w
    ans = max(ans, dp1[x] + dp2[x])
# O(n)

from collections import defaultdict
n = int(input())
dp1 = [0] * n # 从当前点为根节点出发能延生的最长距离
dp2 = [0] * n

# 邻接表存树的结构...
t = defaultdict(list)

dfs(1, 0) # 一般从根节点出发, 但是从哪个节点出发答案都是一样