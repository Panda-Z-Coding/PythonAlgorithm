'''
首先在看到求最小值的最大值--我们就用二分法去枚举，看哪一种情况符合
小了往大了找，大了往小了找

这道题目求解的是士兵的力量值中最小的最大值
- 那我们就定义mid: 士兵力量值中最小的最大值，通过一个函数来检测最终
花费的体力时候能否小于等于k，如果可以的话就返回True。那说明可以达到
可以达到就增大mid，直到二分到最后就是答案。

- 那么我们只要解决如何去编写 判断函数check()？
- - 对于士兵i 如果他的初始力量值小于mid 那么就要训练士兵i
- - 并且我们要知道把这个士兵训练提升 mid - a[i] 的力量值要花费的体力
- - 如果把所有小于mid 的士兵都提升mid-a[i] 花费的体力小于等于k那么就是可以的

- 那么我们如何去求解把士兵i提升 mid-a[i] 要花费的体力？
- - 定义dp[j] 表示: 提升j要花费的最少体力 （就根据需求定义）
- - 转移方程: dp[j] = min(dp[j], dp[max(0, j - b[i])] + c[i])
- - - max(0, j - b[i]) 因为不能小于0

- 那么这道题就剩下二分枚举的范围没确定了
- - 我们看到 k,a,b,c 都是小于等于100， 我们取最大的情况100，就能看出
二分范围  0 <= N <= 100*100 + 100 =>> 10100

'''
def il():
    return list(map(int, input().split()))
N = 10100 # 表示最大的答案可能值
inf = float('inf')
n, m, k = map(int, input().split())
a = [0] + il()
b = [0] + il()
c = [0] + il()

# dp
dp = [inf] * (N)
dp[0] = 0 # 提升0力量花费为0

# 填充dp

for i in range(1, m + 1): # 每一种计划都遍历
    for j in range(N): # 完全背包
        dp[j] = min(dp[j], dp[max(0, j - b[i])] + c[i])

def check(mid):
    # 检查mid能不能在k 内实现
    cost = 0
    for i in range(1, n + 1):
        if a[i] >= mid:
            continue
        cost += dp[mid - a[i]] # 把这个没有mid 大的士兵训练到mid 到花费
    return cost <= k

# 二分查找最小的最大值

l, r = 1, N - 1
while l < r:
    mid = (l + r + 1) // 2
    if check(mid):
        l = mid
    else:
        r = mid - 1

print(l)













