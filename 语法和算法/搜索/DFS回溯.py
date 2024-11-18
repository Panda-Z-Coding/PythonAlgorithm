'''
给一个数,输出它的所有排列

--》 组合树
'''

def dfs(depth):
    # depth : 第depth位数字
    
    if depth == n:
        print(path)
        return
    
    for i in range(1, n + 1):
        # 选择没有标记的数字
        if vis[i]:
            continue
        
        #第depth位数字选择 i
        #! 先打标记
        vis[i] = True
        #! 记录路径
        path.append(i)
        #! 下一层
        dfs(depth + 1)
        #! dfs后面的代码说明已经返回上一层了
        vis[i] = False
        #! 路径重置
        path.pop(-1)

n = int(input())
vis = [False] * (n+1)
path = []
dfs(0)

'''
子集
'''
path = []
def dfs(depth):
    
    if depth == n:
        print(path)
        return
    
    #选
    path.append(a[depth])
    dfs(depth + 1)
    path.pop(-1)
    
    #不选
    dfs(depth + 1)
    
n = int(input())
a = list(map(int, input().split()))
dfs(0)