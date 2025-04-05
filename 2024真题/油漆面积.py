##import os
##import sys
##input = sys.stdin.readline
##
### n个线段树???
##
### 先试一下暴力
##n = int(input())
##maxn = int(1e4 + 5)
##a = [[0] * maxn for i in range(maxn)]
##
##for k in range(n):
##    x1, y1, x2, y2 = map(int, input().split())
##    for i in range(x1, x2):
##        for j in range(y1, y2):
##            a[i][j] = 1
##ans = 0
##for s in a:
##    ans += sum(s)
##print(ans)

#! 扫描线算法
import bisect

def rectangle_area(rectangles):
    # 1. 准备所有垂直边
    events = []
    x_coords = set()
    for x1, y1, x2, y2 in rectangles:
        events.append((y1, x1, x2, 1))   # 入边
        events.append((y2, x1, x2, -1))  # 出边
        x_coords.add(x1)
        x_coords.add(x2)
    
    # 2. 离散化x坐标
    sorted_x = sorted(x_coords)
    x_indices = {x: i for i, x in enumerate(sorted_x)}
    
    # 3. 按y坐标排序所有边
    events.sort()
    
    # 4. 初始化线段树
    n = len(sorted_x)
    count = [0] * (4 * n)  # 区间覆盖次数
    length = [0] * (4 * n)  # 区间有效长度
    
    def update(u, ul, ur, l, r, val):
        '''
        u: 当前线段树节点
        ul: 节点管理的左区间
        ur: 节点管理的右区间
        l: 要更改的左区间
        r: 要更改的右区间
        val: 更新的值
        '''
        if l >= ur or r <= ul:
            return
        if l <= ul and ur <= r:
            count[u] += val
        else:
            um = (ul + ur) // 2
            update(2*u+1, ul, um, l, r, val)
            update(2*u+2, um, ur, l, r, val)
        
        # 更新当前区间的有效长度
        if count[u] > 0:
            length[u] = sorted_x[ur] - sorted_x[ul]
        else:
            if ur - ul == 1:
                length[u] = 0
            else:
                length[u] = length[2*u+1] + length[2*u+2]
    
    # 5. 扫描处理
    total_area = 0
    prev_y = events[0][0]
    
    for y, x1, x2, val in events:
        # 计算当前扫描线与前一条扫描线之间的面积
        total_area += (y - prev_y) * length[0]
        
        # 更新线段树
        l = bisect.bisect_left(sorted_x, x1)
        r = bisect.bisect_left(sorted_x, x2)
        update(0, 0, n-1, l, r, val)
        
        prev_y = y
    
    return total_area
n = int(input())
rectangles = []
for i in range(n):
    rectangles.append(tuple(map(int, input().split())))
print(rectangle_area(rectangles))
