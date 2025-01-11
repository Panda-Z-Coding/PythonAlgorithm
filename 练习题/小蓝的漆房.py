import os
import sys
from collections import Counter
# 请在此输入您的代码

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    color = list(map(int, input().split())) # 每个房子的颜色
    # 利用Counter来算出最多的那一个元素
    Count = Counter(color) #! 错误原因: 不一定取最多的来就是最少时间，每一个都要遍历一遍是最保险的
    most = Count.most_common(1)[0][0] # Count.most_common(1)返回的是一个list, most就是最多的那一个颜色
    # 记录天数
    ans = 0
    
    '''遍历color，找到第一个不是most颜色的房子，然后向后k个变成most'''
    for i in range(0,n - 1):
        # i表示下标位置
        if color[i] != most:
            for j in range(k):
                if i + j >= n: # 边界
                    break
                color[i + j] = most
            ans += 1        
    print(ans)
    
import os
import sys

# 请在此输入您的代码
t = int(input())

for time in range(t):
    n, k=list(map(int, input().split()))
    crd=list(map(int, input().split()))
    #统计有几种颜色
    color=list(set(crd))
    #用于添加刷成各种颜色需要几天
    days=[]
    #尝试刷成每一种颜色
    for i in color:
        crd_copy = crd[:]
        day = 0
        #从第一个位置开始，如果颜色不一样，则刷一段长度为k的区间
        for j in range(n): 
            if crd_copy[j] != i:
                for a in range(j, min(j + k, n)):#区间长不能大于n
                    crd_copy[a]=i
                j=j+k-1 #跳至下一段
                day+=1
        days.append(day)
    #输出最少天数方案
    print(min(days))