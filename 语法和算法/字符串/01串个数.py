# 复习一次

# 首先看到01串，一般都是状态压缩，用二进制去表示

# 任意5个位置中不超过3个位置的值为1的方案数
# “方案数” => 要想到动态规划，去累计方案

# 1. 什么是状态？
# 发现我们只需要关注最后面5个位置的情况是否符合，再往前的就影响不到我们扩展，可以直接转移过来
# dp[i][mask] => 表示前i个位置最后5位的情况是mask 的合法方案数; 这个i也是长度的意思

# 2. 状态转移？
# 可以在结尾尝试添加0或者1，看新的mask符不符合，符合的话就直接累加前面的方案数
# dp[i][mask] += dp[i-1][old_mask] => 所有老的状态添加0或者1能到达当前的mask的方案数都转移过来

# 3. 答案？
# sum(dp[n][mask] if is_valid_mask(mask))

def is_valid_mask(mask):
    return bin(mask).count('1') <= 3


n = 24
window = 5 # 窗口大小

dp = [[0] * (1 << window) for _ in range(n + 1)]

# 初始化，边界情况
for mask in range(1 << window):
    if is_valid_mask(mask):
        dp[window][mask] = 1

# 状态转移
for i in range(window + 1, n + 1):
    for mask in range(1 << window):
        # 枚举mask的所有情况
        if is_valid_mask(mask):
            for bit in [0, 1]:
                old_mask = ((mask << 1) | bit) & ((1 << window) - 1) # 先在右边添加bit再截断
                # (1 << window) - 1 == (11111) == 31
                # 想要截断某一个二进制数 ==> & ((1 << l) - 1)  ## l是截断之后的长度
                if is_valid_mask(old_mask):
                    dp[i][mask] += dp[i-1][old_mask]

res = sum(dp[n][mask] for mask in range(1 << window) if is_valid_mask(mask))
print(res)




