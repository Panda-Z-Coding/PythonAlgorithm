
#? x * (tot - x) 要让这个值最大
# 那么我们需要 让 x和(tot - x) 最相近
# 我们可以枚举出所有x的可能值, 然后再遍历取最大

# dp[x] == 1 => x 是能从数组中凑出来的 
# dp[x] == 0 => x 不能从数组中凑出来的
# 状态转移 => 有点像01背包 => 如果取当前的xx的话我可以从 dp[x - xx] 转移过来
# 边界: dp[0] = 1 => x = 0

a = [
    5160, 9191, 6410, 4657, 7492, 1531, 8854, 1253, 4520, 9231,
    1266, 4801, 3484, 4323, 5070, 1789, 2744, 5959, 9426, 4433,
    4404, 5291, 2470, 8533, 7608, 2935, 8922, 5273, 8364, 8819,
    7374, 8077, 5336, 8495, 5602, 6553, 3548, 5267, 9150, 3309,
]

tot = sum(a)

dp = [0] * (tot + 1)

dp[0] = 1  
for i in range(40):
    for j in range(tot, a[i] - 1, -1): # 逆序遍历是为了保护前面的状态
        dp[j] |= dp[j - a[i]]

# 遍历取最值
ans = 0
for x in range(tot + 1):
    if dp[x]:
        # 如果能被构造
        ans = max(ans, x*(tot - x))
print(ans) 
# 12873625444