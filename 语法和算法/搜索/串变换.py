# 给出k个操作, 可以任意组合来执行, 只要有存在符合的直接return Yes

n = int(input())
S = [int(i) for i in input()]
T = [int(i) for i in input()]
k = int(input())
vis = [False] * k # 用于判断操作是否用过
fin = False # 用于判断是否达到相同
ops = []
for i in range(k):
    ops.append(list(map(int, input().split())))

def dfs():
    global fin, S
    if S == T:
        fin = True
        return
    if fin:
        return
    
    for i in range(k):
        # 遍历所有的操作
        # 如果这个操作没有被使用
        if not vis[i]:
            op, x, y = ops[i]
            vis[i] = True #! 插旗
            # 进行操作
            if op == 1:
                S[x] = (S[x] + y) % 10
                # 去在一层
                dfs()
                S[x] = (S[x] - y + 10) % 10 # 回溯状态
            else: # op == 2
                S[x], S[y] = S[y], S[x]
                dfs()
                S[x], S[y] = S[y], S[x]
            # 回溯当前的操作, 设置为没用哟
            #! 能运行到这里搜索树已经到达了最底层, 这时候应该回溯上去求别的方案, 所以要还原现场
            vis[i] = False #! 拔棋
dfs()
print('Yes' if fin else 'No')