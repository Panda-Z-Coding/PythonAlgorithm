from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

n = int(input())
a = [0] + list(map(int, input().split()))

# 用defualtdict(list) 来充当树边映射关系
e = defaultdict(list)
st = set(range(1, n + 1))

for _ in range(n - 1):
    x, y = map(int, input().split())
    e[y].append(x) # x是y的子节点
    st.discard(x) # x有父节点就不会是根节点

rt = st.pop()
dp = [[0, 0] for i in range(n + 1)]

def dfs(u):
    # u表示当前的节点
    for v in e[u]:
        # 遍历当前节点的所有子节点
        dfs(v)
        dp[u][1] += dp[v][0]
        dp[u][0] += max(dp[v][1], dp[v][0])
    dp[u][1] += a[u] # 选择的话再加上当前节点的权值

dfs(rt)
print(max(dp[rt][0], dp[rt][1]))
