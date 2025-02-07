'''
什么是状态?
为什么不能用前i个的子序列推出后面的状态

1 3 4 2 3 5 6 8 -> 很难找到转移方程

以第i个数字结尾的最长上升子序列
dp[i] = max(dp[j] + 1; j < i && a[j] < a[i])
知道每个子序列尾部信息,并且又是上升的,就能知道

dp[i] 可以从 dp[1]...dp[i-1] 转移, 并且保证a[i] 要比前一个大

'''

'''
同样的我们也可以求最长下降子序列
dp2[i] -> 以i为出发点的最长下降子序列 -> 因为是递减的, 我们确定出发点, 那后面的数字都要比前面的数字小

if j > i and a[j] < a[i]:
    dp2[i] = max(dp2[i], dp2[j] + 1)
'''
n = int(input())
#! !!!! 不要忘记下标要从1开始 !!!!
a = [0] + list(map(int, input().split()))
dp2 = [0] + [1] * n
#? 因为我们是拿后面的情况去更新前面的, 所以要从后往前遍历
#? 这个是最长下降子序列
for i in range(n, 0, -1):
    for j in range(i + 1, n + 1):
        if a[j] <= a[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
print(max(dp2))

'''
合唱队形: 又上升又下降的最长
'''
dp = [0] + [1] * n
#! 最长上升子序列
for i in range(1, n + 1):
    for j in range(1, i):
        #? 在i的前面找到小于a[i] 的数字 a[j]
        if a[j] <= a[i]:
            # a[i]要比前一个大
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp)) # 答案