# 假设有n件商品，每件商品的体积是t + 1，价值是c
# 我们要找到物品数量至少为n的，花费最少的方案

# 定义dp[j] -> 前j个物品花费的最少费用

n = int(input())

ts = [0]
cs = [0]

for i in range(1, n + 1):
    ti, ci = map(int, input().split())
    ts.append(ti + 1) # 买单要ti的时间, 可以拿走ti个，再加上本身的
    cs.append(ci)
v = max(ts) + n 

dp = [float('inf')] * (v + 1)

dp[0] = 0 # 前0个物品花费0元

for i in range(1, n + 1):
    for j in range(v, ts[i] - 1, -1):
        dp[j] = min(dp[j], dp[j - ts[i]] + cs[i]) # 拿: 可以多拿ts[i]个，但是要多花前
        # 不拿就原本多少钱就多少钱

ans = min(dp[n: v+1]) # 至少为n个物品
print(ans)
