import os
import sys

# 请在此输入您的代码
# def AllTime(a):
#     result = 1
#     for num in a:
#         result *= num
#     return result


t = int(input())
for _ in range(t):
    n = int(input())
    value = list(map(int, input().split()))
    # 乘积、和不为零
    # 只能 +1, 那就直接暴力
    ans = 0
    '''先把0找出来变成1, 然后直接暴力加'''
    for i in range(n):
        if value[i] == 0:
            value[i] += 1
            ans += 1
    '''如果和为零就随便加一个1都能使的和不为零'''
    
    if sum(value) == 0:
        ans += 1
    print(ans)
        