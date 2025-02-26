import os
import sys
from collections import deque   

def ii():
    return sys.stdin.readline()
def il():
    return map(int, sys.stdin.readline().split())
# 用来记录有没有走过，并且每次走到这里要更新当前的无敌步数
# 定义一个node节点
class node(): # 用node节点来存储每个点的信息，就不用像数组一样要去看第几个是什么参数
    def __init__(self, x, y, step, magic):
        self.x = x
        self.y = y
        self.step = step # 当前的步数
        self.magic = magic # 当前的无敌步数

def bfs():
    '''
    bfs剪支+条件判断
    特殊一点的是无敌步数，我们可以先判断常规的情况 => 越界、有没无敌步数
    然后我们计算当前节点的无敌步数
    之后判断特殊的情况 => 是不是%、当前节点的无敌步数是不是比较少、是不是墙
    '''
    q = deque()
    q.append(node(0, 0, 0, 0))
    while q:
        cur = q.popleft()

        # 循环出口
        if cur.x == n-1 and cur.y == n-1:
            print(cur.step)
            break

        # 访问所有合法的节点
        for dx, dy in dic:
            x = cur.x + dx
            y = cur.y + dy
            # 是否越界
            if not(0 <= x < n and 0 <= y < n): # n * n 地图！！
                continue

            # 有没有无敌,没有无敌步数不能走-Coninue
            if Map[x][y] == 'X' and cur.magic == 0:
                continue

            magic = max(0, cur.magic - 1) # 最小是0
            # 运行到这里就是走了一步了，无敌步数要减少

            if Map[x][y] == '%':
                # 遇到% 重置无敌步数
                magic = k

            if vis[x][y] < magic and Map[x][y] != '#': #! 剪支
                # 要去到的点，要比现在的无敌步数少，并且不是墙；
                #? 去无敌步数少的是为了不走回头路，因为来时候的路肯定跟多步数
                
                vis[x][y] = magic
                q.append(node(x, y, cur.step + 1, magic))
                # 到达这里就是满足所有的
                # 步数加一，更新无敌步数

n, k = il()
Map = [input() for i in range(n)]
vis = [[-1] * n for i in range(n)]
vis[0][0] = 0
dic = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 移动方向

bfs()
