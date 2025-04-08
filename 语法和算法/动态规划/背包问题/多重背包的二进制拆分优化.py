N, V = map(int, input().split())
w_v = []

for i in range(N):
    w, v, s = map(int, input().split())
    k = 1
    while s >= k:
        w_v.append((k * w, k * v))
        s -= k
        k <<= 1
    #? 如果有剩余
    if s != 0:
        w_v.append((s * w, s * v))
# 正常的01背包做法
dp = [0] * (V + 1)
for i, (w, v) in enumerate(w_v):
    # 取出当前物品的重和价值
    for j in range(V, w - 1, -1): # 倒序遍历
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[V])

# for i in range(len(w_v)):
#     w, v = w_v[i]