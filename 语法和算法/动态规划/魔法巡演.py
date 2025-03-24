##import os
##import sys
##input = sys.stdin.readline
##
##def check(x):
##    if '0' in str(x) or '2' in str(x) or '4' in str(x):
##        return True
##    else:
##        return False
##
##n = int(input())          
##
##s = [1] + list(map(int, input().split()))
### s = [x for x in s if ('0' in str(x) or '2' in str(x) or '4' in str(x))]
##
##t = [1] + list(map(int, input().split()))
##
##dp1 = [[0] * (n + 1) for i in range(n+1)]
##dp2 = [[0] * (n + 1) for i in range(n + 1)]
##
##
##
##for i in range(1, n + 1):
##    if check(s[i]):
##        # 当前数字能选择
##        # 选
##        dp1[i][1] = max(dp1[i-1][0], dp1[i-1][1]) + 1
##        # 不选
##        dp1[i][0] = max(dp1[i-1][0], dp1[i-1][1])
##    else:
##        # 当前数字不能选择
##        continue
##    j = min(i + 1, n) # 开始选择t
##    if check(t[j]):
##        dp2[i][1] = max(dp2[i-1][0], dp2[i-1][1]) + 1
##        dp2[i][0] = max(dp2[i-1][0], dp2[i-1][1])
##    else:
##        continue
##    i = min(j + 1, n)
##
##
##print(max(dp1[n][0], dp1[n][1]) + max(dp2[n][0], dp2[n][1]))

# ==dp的定义错的离谱==

# 动态规划的非法状态初始化，负无穷的状态表示这个状态是不存在的不可能的
import os
import sys
input = sys.stdin.readline

#! 连续两个使用的石头要有共鸣元素


n = int(input())

s = [1] + list(map(int, input().split())) # 下标从1开始
t = [1] + list(map(int, input().split()))

'''
dps[i][j] => 前i个石头中，最后一个来自s序列且包含共鸣元素j的最长序列
dpt[i][j] => 前i个石头中，最后一个来自t序列且包含共鸣元素j的最长序列

j => {0: 0, 1: 2, 2: 4}

为了处理不能选择的情况，我们先对把上一个状态全部转移过来
之后再把当前数字上有的共鸣元素都取出来，进行状态转换

当我们遍历到i的时候如果轮到小蓝选择，那么要从dpt中选择能影响到这次选择的几个dp值进行最大更新

'''
# 定义状态
dps = [[-float('inf')] * 3 for i in range(n + 1)] # 下标从1开始
dpt = [[-float('inf')] * 3 for i in range(n + 1)] 
# 负无穷表示当前状态不可达
# 若初始化为0，当符文石不包含共鸣元素时，状态会错误继承前序的0值
#? 如果是求最小的步数之类的 => 初始化非法状态为无穷
def f(x):
    if x == 0:
        return 0
    if x == 2:
        return 1
    if x == 4:
        return 2

# 规定边界
# dp[1][j] = 0

for j in range(3):
    dpt[0][j] = 0
    # 因为小蓝先开始，所以dps[0][j] 是无法到达的状态表示成负无穷
    #! 真正的起点是小桥
   

# 遍历dp
for i in range(1, n + 1):
    for j in range(3):
        dps[i][j] = dps[i-1][j]
        dpt[i][j] = dpt[i-1][j]
    
    x_s, x_t = s[i], t[i]

    di = set()
    while x_s:
        digit = x_s % 10
        if digit in {0, 2, 4}:
            di.add(f(digit))
        x_s //= 10
    
    # 当前处理s, 就从dpt转移过来
    w = -float('inf')
    for j in di:
        w = max(w, dpt[i-1][j])
    
    # 遍历当前的dps
    for j in di:
        dps[i][j] = max(dps[i][j], w + 1)

    di.clear()
    w = -float('inf')

    # 处理t
    while x_t:
        digit = x_t % 10
        if digit in {0, 2, 4}:
            di.add(f(digit))
        x_t //= 10

    for j in di:
        w = max(w, dps[i-1][j])

    for j in di:
        dpt[i][j] = max(dpt[i][j], w + 1)  
print(*dps, sep='\n')
print()
print(*dpt, sep='\n')
print(max(max(dps[n]), max(dpt[n])))
