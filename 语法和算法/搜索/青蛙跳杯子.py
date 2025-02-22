# W 字母表示白色青蛙，B 表示黑色青蛙，∗ 表示空杯子

# 每个青蛙能做三个动作其中之一
# 1. 跳到相邻的空杯子
# 2. 隔着一只青蛙跳到空杯子
# 3. 隔着两只青蛙跳到空杯子
# 其实就是跳到空杯子 - 只能条1,2,3格

# 问至少要几步能跳成指定的情况

# bfs能确保第一次到达这种情况的是最短路

from collections import deque

move = [1,-1,2,-2,3,-3] # 左右跳

x = input()
y = input()
visited = set()
visited.add(x)
len_x = len(x)
def bfs():
    # 从最原始开始bfs
    q = deque([(x, 0)]) # 记录出现的字符串，和走过的步数
    while q:
        old = q.popleft()
        for i in move:
            st = list(old[0])
            step = old[1]
            empty_in = st.index('*')
            ii = i + empty_in
            if 0 <= ii < len_x:
                st[empty_in] = st[ii]
                st[ii] = '*'
                e = "".join(st)
                step += 1
                if e == y:
                    print(step)
                    return
                if e not in visited:
                    visited.add(e)
                    q.append((e, step))

bfs()