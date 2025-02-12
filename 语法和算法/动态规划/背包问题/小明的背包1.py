# 小明的背包1
N, V = map(int, input().split())
weights = []
values = []

for i in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# 初始化dp
dp = [0] * (V + 1)  
for i in range(n):
    for j in range(V, weights[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

print(dp[V])
