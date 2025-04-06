import os
import sys
input = sys.stdin.readline
# DFS求最大路径
# 向左下走的次数与向右下走的次数相差不能超过 1 -> 剪枝条件
# 每次走的位置 (1, 0), (1, 1)
n = int(input())
mp = [[-1] * (n + 1) for i in range(n + 2)] #下标都要从1开始
for i in range(1, n + 1):
    row = [-1] + list(map(int, input().split())) + [-1] * (n + 1 - i)
    mp[i] = row
print(*mp, sep = '\n')
ans = 0
##r_cnt = 0
##l_cnt = 0 # 作为全局上下文
##vis = set()
def dfs(x, y, cur_s, l_cnt, r_cnt):
    global ans
    # 剪枝条件
    # if x > n + 1 or x < 1 or y > n + 1 or y < 1: return
    if abs(l_cnt - r_cnt) > 1: return
    if mp[x][y] == -1: return 
    # 先写退出条件
    if x == n + 1 and abs(l_cnt - r_cnt) <= 1:
        ans = max(ans, cur_s)
        # print(1) 这个if没有进来???
        return
    ans = max(ans, cur_s)
    # 扩展
    # 先向左下走
    dfs(x + 1, y, cur_s + mp[x][y], l_cnt + 1, r_cnt)
    # 后向右下走
    dfs(x + 1, y + 1, cur_s + mp[x][y], l_cnt, r_cnt + 1)
    
dfs(1, 1, mp[1][1], 0, 0)
print(ans)


    
