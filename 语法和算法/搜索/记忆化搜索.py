'''
- 通过记录已经遍历过的状态信息,从而避免重复遍历
- dfs + 字典
'''
import sys
sys.setrecursionlimit(100000)
# 斐波那契

from functools import lru_cache
@lru_cache(maxsize=None)
def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n-1) + f(n-2)
# 这样就会有很多的重复计算
#! 加上 @lru_cache(maxsize = None) 就自动记忆化搜索了

# 每次搜索把当前状态存进字典
dic = {0:1, 1:1}
def f1(n):
    if n in dic.keys():
        return dic[n]
    dic[n] = (f1(n-1) + f1(n-2)) % 100000007
    return dic[n]

n = int(input())
a = f(n)
print(a)

#TODO 例题: 3820

import os
import sys
from functools import lru_cache
# 请在此输入您的代码
@lru_cache(maxsize = None)
def dfs(x, y, z):
    """
    x,y -> 当前的位置
    z -> 是否使用！过！背包
    """

    if x == c and y == d:
        return True

    # 若没走到终点,玩四个方向走
    for delta_x, delta_y in [(1,0), (-1,0), (0, 1), (0, -1)]:
        xx, yy = x + delta_x, y + delta_y

        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        
        if Map[xx][yy] < Map[x][y]:
            if dfs(xx, yy, z):
                return True
        # Map[x][y] + k表示原地升高k后,若比下一个点高的话就是可以走到下一个点,并且标记背包被使用
        elif z == False and Map[xx][yy] < Map[x][y] + k:
            if dfs(xx, yy, True):
                return True
    #这个点四周都不能出去
    return False

n, m, k = map(int, input().split())
a, b, c, d = map(int, input().split())
a, b, c, d = a - 1, b - 1, c - 1, d - 1
Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))
    
if dfs(a, b, False):
    print("Yes")
else:
    print("No")
    
'''
地宫取宝 - 216
'''
@lru_cache(maxsize = None)
def dfs(x, y, z, w):
    """
    (x,y):      当前坐标
    z:          先前拿到的宝贝数量
    w:          先前宝贝的最大价值
    return:     从当前状态出发的方案数
    """
    if x == n - 1 and y == m - 1:
        # 在终点不拿东西
        if z == k:
            return 1
        # 在终点拿东西
        if z == k - 1 and w < Map[x][y]:
            return 1
        return 0

    # 两个方向
    # 方案数: 右边的 + 下面的, 两个方向
    ans = 0
    for delta_x, delta_y in [(0,1),(1,0)]:
        # 下标不越界
        xx, yy = x + delta_x, y + delta_y
        if xx < n and yy < m:
            # 当前不选择宝物，走到(xx,yy)
            ans += dfs(xx, yy, z, w)

            # 当前选择宝物， 走到(xx,yy)
            if w < Map[x][y]:
                ans += dfs(xx, yy, z + 1, Map[x][y])
            ans %= 1000000007
    return ans  
    
n, m, k = map(int, input().split())
Map = []
for _ in range(n):
    Map.append(list(map(int, input().split())))
print(dfs(0, 0, 0, -1))