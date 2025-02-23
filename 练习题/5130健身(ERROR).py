import os
import sys

#! ERROR !!

# 请在此输入您的代码

n, m, q = map(int,input().split())
ans = 0
# 初始化列表,让全部都为1（表示有空的天数）,没空的就赋值0
days = [1 for _ in range(n)]
a = list(map(int, input().split()))
for i in range(q):
    days[a[i] - 1] = 0

# 计算连续天数，存入数组里面
free_days = []
day = 0
b = 0
for i in days:
    
    if i:
        day += 1
    if (not i or b == len(days) - 1) and day != 0:
        free_days.append(day)
        day = 0
    b+=1
    
    
    # if days[i] == 1 and i != len(days) - 2:
    #     day += 1
    #     print(day)
    # if days[i] == 0 and day != 0:
    #     free_days.append(day)
    #     day = 0
    # if i == len(days) - 2 and days[i] == 1 and day == 1:
    #     free_days.append(day)
    # if i == len(days) - 2 and days[i] == 1 and day == 0:
    #     free_days.append(1)
free_days.sort()       
# print(free_days) 
fitness = []
for i in range(m):
    fitness.append(list(map(int, input().split())))
    fitness[i][0] = 2**fitness[i][0]
# 按照收益来排序，从大的开始便利，该有没有可以满足的连续天数
fitness.sort(key= lambda x:x[1],reverse=True)

for fit in fitness:
    if len(free_days) == 0:
        break
    if fit[0] <= free_days[-1]:
        ans += fit[1]
        free_days[-1] -= fit[0]
        if free_days[-1] == 0:
            free_days.pop(-1)
        free_days.sort()
        
print(ans)