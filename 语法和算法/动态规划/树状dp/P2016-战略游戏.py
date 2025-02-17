from collections import defaultdict
import sys
n = int(input())
e = defaultdict(list)# 映射树边关系
st = set(range(n))
for i in range(n):
    inf = list(map(int, input().split()))
    if inf[1] == 0:
        continue
    for j in inf[2:2+inf[1]]:
        e[inf[0]].append(j)
        st.discard(j)
rt = st.pop()

#定义dp[u][1]-> 选取这个点的最小权
# dp[u][0] -> 不选择这个点的最小权

dp = [[0, 0] for i in range(n+1)]

def dfs(u):
    # u表示当前节点
    # 先遍历所有子节点求解
    for v in e[u]:
        dfs(v)
        dp[u][0] += dp[v][1]
        dp[u][1] += min(dp[v][1], dp[v][0])
    dp[u][1] += 1

dfs(rt)
print(min(dp[rt][0], dp[rt][1]))