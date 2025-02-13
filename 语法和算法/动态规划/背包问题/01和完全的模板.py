#? 01: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

#? 完全: dp[i][j] = max(dp[i-1][j], dp[i][j-w] + v)

def dp_01(W, wt, val, n):
    """
    :param W: 背包的总容量
    :param wt: 物品的重量列表，wt[i]表示第i个物品的重量
    :param val: 物品的价值列表，val[i]表示第i个物品的价值
    :param n: 物品的总数量
    :return: 背包能装下的最大价值
    """
    dp = [0] * (W + 1)
    for i in range(n):
        # 逆序遍历，确保每个物品只被选取一次
        for j in range(W, wt[i] - 1, -1): #? 确保背包容量j大于等于wt[i]
            dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
    return dp[W]

def dp_Complete(W, wt, val, n):
    """
    :param W: 背包的总容量
    :param wt: 物品的重量列表，wt[i]表示第i个物品的重量
    :param val: 物品的价值列表，val[i]表示第i个物品的价值
    :param n: 物品的总数量
    :return: 背包能装下的最大价值
    """
    dp = [0] * (W + 1)
    for i in range(n):
        # 正序遍历，允许每个物品被多次选取
        for j in range(wt[i], W + 1):
            # j >= wt[i]: 当前背包的容量要大于等于物体的重量才有用
            dp[j] = max(dp[j], dp[j - wt[i]] + val[i])
    return dp[W]

