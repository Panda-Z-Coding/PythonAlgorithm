class TreeArray():
    # 初始化
    def __init__(self, l):
        self.data = [0] * l
        # 树状数组的下标要从1开始

    # lowbit(x)
    def lowbit(self, x):
        return x & (-x)

    # # add(w)
    # def add(self, w):
    #     # 树状数组的更新操作
    #     while w <= MAX:
    #         self.data[w] += 1
    #         w += self.lowbit(w)
    #? 根据题目来制定更新计划
    
    def add(self, index, x):
        while index <= len(self.data):
            self.data[index] += x
            index += self.lowbit(index) 

    # query
    def query(self, w):
        # 查询当前宽度之前有多少个已经遍历过的矩形
        s = 0
        while w > 0:
            s += self.data[w]
            w -= self.lowbit(w)
        return s