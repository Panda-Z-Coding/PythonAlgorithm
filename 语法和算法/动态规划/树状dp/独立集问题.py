# from collections import defaultdict

# class TreeNode:
#     def __init__(self, val = 0):
#         self.val = val
#         self.children = []

# def max_independent_set(root):
#     #! 自底向上
#     dp = defaultdict(lambda: [0, 0])
#     #? dp[u][1]: 表示选择这个节点
#     #? dp[u][0]: 表示不选择这个节点
#     def dfs(u):
#         #? 对每一个节点进行dfs求解出它所有子树的最大独立集
#         dp[u][1] = u.val 
#         for v in u.children:
#             dfs(v)
#             dp[u][0] += max(dp[v][1], dp[v][0]) #? 不选择当前节点就可以把它的所有子节点的最大独立集加进来
#             dp[u][1] += dp[v][0] #? 选择当前节点就把它所有子节的不选状态的独立集加过来
#     dfs(root)
#     return max(dp[root][1], dp[root][0])

#! defaultdict(list) 可以充当C++ 的vector<int> e[N]

from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)  # 设置递归深度限制

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a  # 将索引从1开始
    
    # 初始化邻接表
    e = defaultdict(list) # vector e[N]
    st = set(range(1, n + 1))  # 所有可能的根节点
    
    # 构建树
    for _ in range(n - 1):
        x, y = map(int, input().split())
        e[y].append(x)  # y是x的直接上司
        st.discard(x)  # x有父节点，说明不是根节点，删除
    
    rt = st.pop()  # 最后剩下的就是父节点
    
    # 初始化dp数组
    dp = defaultdict(lambda: [0, 0])
    
    def dfs(u):
        for v in e[u]:
            dfs(v)
            dp[u][1] += dp[v][0]  # 选择u，不能选择其子节点
            dp[u][0] += max(dp[v][0], dp[v][1])  # 不选择u，可以选择或不选择子节点
        dp[u][1] += a[u]  # 加上u的权值
    
    dfs(rt)
    print(max(dp[rt][0], dp[rt][1]))

if __name__ == "__main__":
    main()