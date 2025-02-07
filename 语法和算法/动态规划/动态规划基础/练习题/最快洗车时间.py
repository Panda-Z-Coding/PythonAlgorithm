# 读取输入的车辆数量
n = int(input())

# 读取每辆车的洗车时间，并存储在一个列表中
car = list(map(int, input().split()))

# 计算所有车洗车时间的总和的一半
# 目标是将洗车时间尽可能均等地分配到两台洗车器上
target = sum(car) // 2

# 初始化动态规划数组 dp
# dp[i] 表示在容量为 i 的情况下，可以达到的最大洗车时间
dp = [0] * (target + 1)

# 遍历每辆车的洗车时间
for value in car:
    # 从 target 开始倒序遍历到 value
    # 这是为了确保每个车辆的洗车时间只被考虑一次
    for i in range(target, value - 1, -1):
        # 更新 dp[i]：选择是否将当前车的洗车时间 value 加入
        # dp[i] = max(dp[i], dp[i - value] + value)
        # dp[i] 表示当前容量为 i 时的最大洗车时间
        # dp[i - value] + value 表示在容量为 i - value 时的最大洗车时间加上当前车的洗车时间
        dp[i] = max(dp[i], dp[i - value] + value)

# 最后，计算两台洗车器中洗车时间的最大值
# dp[-1] 表示在容量为 target 的情况下，可以达到的最大洗车时间
# sum(car) - dp[-1] 表示另一台洗车器的洗车时间
# 取两者的最大值，即为关闭电源所需的最少时间
print(max(dp[-1], sum(car) - dp[-1]))