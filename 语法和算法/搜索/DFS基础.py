'''
dfs搜索策略 && n重循环
'''
def dfs(depth, last_value):
    '''
    depth: 当前处于第dept层
    last_value: 上一个层选的参数
    '''
    if last_value >= x:
        return
    #如果现在进来的值都比 x大，那么可以不用进行下面的循环了
    
    #递归出口
    if depth == n:
        #判断数字之和是否为x
        
        
        
        if sum(path) != x:
            return
        
        print(path)
        return
    
    for i in range(last_value, x + 1):
        path[depth] = i
        dfs(depth + 1, i)

x = int(input())
n = int(input())    
path = [0] * n
dfs(0, 1)

# import os
# import sys

# # 请在此输入您的代码
# ans = 0 

# def dfs(depth, n, m):

#     if depth == 7 and n == 0 and m == 0:
#         global ans
#         ans += 1
#         return

#     #枚举可能性

#     #枚举第一重
#     for i in range(0, 6):
#         for j in range(0, 6):
#             if 2 <= i + j <= 5 and i <= n and j <= m:
#                 dfs(depth + 1, n - i, m - j)

# dfs(0, 9, 16)
# print(ans)