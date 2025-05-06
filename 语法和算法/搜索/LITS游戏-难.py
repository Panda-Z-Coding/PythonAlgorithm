import os
import sys

# 列出12种偏移情况
# 我们列举左上角，看能不能以左上角为原点在不越界是‘1’的情况下都填完

# 这里我们列举的是(x,y)的变化量(dx,dy), 按照最左边的点进行枚举旋转
# 按照左上角确定点
L = [
    [(1,0),(2,0),(2,1)],
    [(0,-1),(0,-2),(1,-2)],
    [(-1,0),(-2,0),(-2,-1)],
    [(0,1),(0,2),(-1,2)]
]

I = [
    [(1,0),(2,0),(3,0)],
    [(0,-1),(0,-2),(0,-3)]
]

T = [
    [(1,0),(0,-1),(0,1)],
    [(1,0),(0,-1),(-1,0)],
    [(0,-1),(0,1),(-1,0)],
    [(-1,0),(0,1),(1,0)]
]

S = [
    [(1,0),(1,-1),(0,1)],
    [(-1,0),(1,1),(0,1)]
]

def check(all_lb, x, y, res, depth):
    # 检查当前位置能不能放置对应的形状的函数
    # all_lb 就是 LITS 中的一种
    for zb in all_lb: # 遍历所有的情况
        for dx, dy in zb:
            if not(0 <= x + dx < n and 0 <= y + dy < n and arr[x + dx][y + dy] == '1'):
                break
        else:
            # for-else 结构 => 如果在for循环里面没有发生break就执行else
            # 说明当前位置可以放置该形状
            for dx, dy in zb:
                arr[x + dx][y + dy] = '0' # 放置了之后设置为0
            arr[x][y] = '0' # 不要忘记出发点
            # 当前形状放好了, 我们进入下一层
            # 同样用res来追踪是否全部满足
            res |= dfs(depth + 1)
            # 回溯
            for dx, dy in zb:
                arr[x + dx][y + dy] = '1'
            arr[x][y] = '1'
    return res


def dfs(depth):
    # depth => 当前在放置哪一个形状 0 1 2 3 -> LITS
    res = False # 追踪是否全部形状能放完
    
    #? 我们进行暴力枚举, 枚举每一个位置为出发点能不能放置当前形状
    for x in range(n):
        for y in range(n):
            if arr[x][y] == '1':
                # 通过判断当前的形状, 就可以不重复判断, 按照LITS顺序放置
                if depth == 0:
                    # 放置L
                    res |= check(L, x, y, res, depth)
                if depth == 1:
                    # 放置I
                    res |= check(I, x, y, res, depth)
                if depth == 2:
                    # T
                    res |= check(T, x, y, res, depth)
                if depth == 3:
                    # S
                    # 这里其实是我们dfs递归的出口
                    for zb in S:
                        for dx, dy in zb:
                            if not(0 <= x + dx < n and 0 <= y + dy < n and arr[x + dx][y + dy] == '1'):
                                break
                        else:
                            # 如果for不发生break, 也就是全部点都符合情况
                            # 放置S
                            res = True
                            # 这里我们直接返回True就行了, 没必要再去寻找别的状态了
                            return res

    return res

# 输入

t = int(input())
for _ in range(t):
    n = int(input())

    arr = [list(input().split()) for i in range(n)]
    print("Yes" if dfs(0) else "No")

