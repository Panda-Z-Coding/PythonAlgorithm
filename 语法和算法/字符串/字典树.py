class TreeNode():
    def __init__(self):
        # nodes 表示往下走的节点
        self.nodes = {}
        # 是否是叶子节点, 是否是字符串终止标志
        self.is_leaf = False

    # 插入字符s
    def insert(self, s):
        curr = self # 当前节点
        for c in s: #遍历字符串

            # 判断当前节点是否有c边
            if c not in curr.nodes.keys():
                curr.nodes[c] = TreeNode()
                # 如果没有c这一条边, 那就创建c边
            
            curr = curr.nodes[c]
        curr.is_leaf = True # 走到叶子了    

    def prex(self, s):
        # 判断前缀s是否存在
        curr = self
        for c in s:
            if c not in curr.nodes.keys():
                return False
            curr = curr.nodes[c] # 往下走
        return True # 能全部走完, 说明存在
