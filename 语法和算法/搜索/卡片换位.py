# 用三元组(A_pos, B_pos, space) -> A_pos = (x, y) 元组套元组来简化语法

g = [[], []]
# 地图
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#输入地图
for i in range(2):
    temp = input()
    for j in range(3):
        g[i].append(temp[j])
        if temp[j] == ' ':
            space = (i, j)
        elif temp[j] == 'A':
            A = (i, j)
        elif temp[j] == 'B':
            B = (i, j)

# 设置一个状态 => （A,B,sapce） # 知道了AB和空格的位置就能锁死这个地图，因为士兵的位置我们不用去管
vis = set() # 看状态是否出现过
queue = [(A, B, space)]
vis.add((A,B,space))
# 标志变量, 看是否找到解
flag = False
cnt = 0 # 步数
while not flag: # 外面一层循环是用来控制步数的
    temp = [] # 用于存储当前层出现的新状态
    # bfs
    while queue:
        a = queue.pop()
        # 获取当前节点的信息
        tempA = a[0]
        tempB = a[1]
        curspace = a[2] # 当前的空格所在地
        # 遍历空格的所有相邻节点
        for dx, dy in dirs:
            x, y = curspace[0] + dx, curspace[1] + dy
            nextnode = (x, y) # 组合成元组，方便比较
            # 判断是否越界和这个新状态没有出现过
            if 0 <= x < 2 and 0 <= y < 3:
                # 当前状态的A，B节点位置
                a = tempA
                b = tempB # 先复制一份方便后续对比
                
                if nextnode == tempA:
                    # 被换位的是A，那a就要换到空格处
                    a = curspace
                elif nextnode == tempB:
                    b = curspace

                # 判断当前是否是目标状态
                if (a, b) == (B, A):
                    flag = True
                    break
                # 如果不是，就看是不是新状态
                if (a, b, nextnode) in vis:
                    continue
                vis.add((a,b,nextnode))
                temp.append((a,b,nextnode))
        
                
    # 遍历完了所有相邻节点后
    queue = temp[:] # 复制一份新状态去到下一层
    cnt += 1
print(cnt)
        
        




















    
