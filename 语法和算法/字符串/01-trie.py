# 特殊的字典树, 用于存二进制数字的

#? 可用于二进制的快速运算判断问题


class TreeNode():
    def __init__(self):
        self.nodes = [None, None] # 左右
        self.is_num = False # 是否走到根节点
        
    def insert(self, s):
        curr = self
        for i in range(31, -1, -1): # 从高位走到低位
            c = (s >> i) & 1 # 每一位都取出来
            if curr.nodes[c] is None:
                curr.nodes[c] = TreeNode()
            curr = curr.nodes[c]
        
        curr.is_num = s # 结尾
    
    def query(self, s):
        # 在01树中查询哪个num => s^num最大
        curr = self
        for i in range(31, -1, -1):
            c = (s >> i) & 1
            # 往反方向走
            if curr.nodes[c ^ 1] is not None:
                curr = curr.nodes[c ^ 1]
            else: # 反方向没有, 正这走
                curr = curr.nodes[c]
        return s ^ curr.is_num
    
n = int(input())

a = list(map(int, input().split()))
q = int(input())

root = TreeNode()
for num in a:
    root.insert(num)

for _ in range(q):
    num = int(input())
    print(root.query(num))