class SegmentTree():
    def __init__(self, arr):
        '''
        - arr: 原始数组
        - n: 数组长度
        '''
        self.arr = [0] + arr[:]
        self.n = len(self.arr)
        self.d = [0] * (4 * self.n) # 线段树数组
        self.lazy = [0] * (4 * self.n) # lazy标志数组
        # 自动调用建树
        self.build(1, self.n - 1, 1) # 因为长度是比原始数组多1的, 所以这里[1, self.n - 1]
    
    def build(self, s, t, p):
        '''
        - fuction: 建树
        - [s, t]: 对于区间[s, t]进行建树
        - p: 根节点的编号
        '''
        if s == t:
            # 区间长度为1, 也就是到达了叶子节点
            self.d[p] = self.arr[s] # 叶子节点都存原数组数值
            return 
        m = (s + t) >> 1 # 求中点
        self.build(s, m, p << 1) # 递归求解左子节点
        self.build(m + 1, t, p << 1 | 1) # 递归求解右子节点
        self.d[p] = self.d[p << 1] + self.d[p << 1 | 1] # 合并子节点的数值
    
    def get_sum(self, l, r, s, t, p):
        '''
        - fuction: 查询区间信息
        - [l, r]: 查询的区间
        - [s, t]: 当前节点包含的区间
        - p: 当前节点编号
        '''
        if l <= s and t <= r:
            # [s, t]∈[l, r]: 直接返回节点值
            return self.d[p]
        m = (s + t) >> 1
        sum_ = 0
        if l <= m:
            # 左边递归
            sum_ += self.get_sum(l, r, s, m, p << 1)
        if r > m:
            sum_ += self.get_sum(l, r, m + 1, t, p << 1 | 1)
        return sum_
    
    def once_update(self, index, value, s, t, p):
        '''
        fuction: 单点更新
        - index: 要操作的下标
        - value: 要更新的值
        - [s, t]: 当前节点包含的区间
        - p: 当前节点编号
        '''
        if s == t:
            # 找到叶子节点, 进行更新
            self.d[p] += value
            return
        m = (s + t) >> 1
        if index <= m:
            self.once_update(index, value, s, m, p << 1)
        else:
            self.once_update(index, value, m + 1, t, p << 1 | 1)
        
        # merge
        self.d[p] = self.d[p << 1] + self.d[p << 1 | 1]
    
    def push_down(self, s, t, p):
        '''
        - fuction: 将lazy标记向下传递给子节点, 并且把自己的lazy标记归零
        - [s, t]: 当前节点包含的区间
        - p: 当前节点编号
        '''
        if self.lazy[p] != 0: #? 如果当前的lazy标志为您则不用更新
            m = (s + t) >> 1
            # 更新左子节点
            self.d[p << 1] += self.lazy[p] * (m - s + 1) # t - m - (m - s + 1) = t + s - 1 -> 区间长度
            self.lazy[p << 1] += self.lazy[p]
            # 更新右子节点
            self.d[p << 1 | 1] += self.lazy[p] * (t - m) 
            self.lazy[p << 1 | 1] += self.lazy[p]

            # 清除当前的lazy标记
            self.lazy[p] = 0
    
    def range_update(self, l, r, value, s, t, p):
        '''
        - fuction: 将[l, r] 的每一个元素都加上value
        - [s, t]: 当前节点包含的区间
        - p: 当前节点编号
        '''
        
        if l <= s and t <= r:
            # [s, t]∈[l, r]
            self.d[p] += value * (t - s + 1) # 乘上这个区间有多少个元素
            # 打上lazy标记
            self.lazy[p] += value # 表示这个区间被操作了value
            return 
        
        self.push_down(s, t, p) # 下放lazy标记
        m = (s + t) >> 1

        if l <= m:
            self.range_update(l, r, value, s, m, p << 1)
        if r > m:
            self.range_update(l, r, value, m + 1, t, p << 1 | 1)
        
        # merge
        self.d[p] = self.d[p << 1] + self.d[p << 1 | 1]

    def get_sum_with_lazy(self, l, r, s, t, p):
        '''
        - fuction: 查询区间信息, 带lazy标记的
        - [l, r]: 查询的区间
        - [s, t]: 当前节点包含的区间
        - p: 当前节点编号
        '''
        if l <= s and t <= r:
            # [s, t]∈[l, r]: 直接返回节点值
            return self.d[p]

        # 在递归查询之前, 先向下去传递lazy标记
        self.push_down(s, t, p)
        
        m = (s + t) >> 1
        sum_ = 0
        if l <= m:
            # 左边递归
            sum_ += self.get_sum_with_lazy(l, r, s, m, p << 1)
        if r > m:
            sum_ += self.get_sum_with_lazy(l, r, m + 1, t, p << 1 | 1)
        return sum_
    
segment = SegmentTree([1, 2, 3, 4, 5])
segment.range_update(2, 4, 5, 1, segment.n - 1, 1)
print(segment.get_sum_with_lazy(2, 4, 1, segment.n - 1, 1))