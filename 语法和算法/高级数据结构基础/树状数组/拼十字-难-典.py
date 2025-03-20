import sys
input = sys.stdin.readline

'''
- 首先明确合法的条件
    - 1. 颜色不同 => 也就是说只能从其他两种颜色选择符合的加过来
    - 2. L_i > L_j and W_i < W_j
    - 这第二个条件才是最麻烦的

- 看第二个条件: 我可以先满足其中一个条件, 另一个我再用别的方法判断
    - 先满足长度大于 => 这里我们可以进行降序排序, 等一下就知道为什么需要降序
    - 如果长度一样的就按照宽度降序

- 在让长度降序排序之后, 我们发现从左到右遍历时候, 当前的一定比之前的要小,
  那么要满足条件的话, 就需要当前的宽度大于之前的宽度, 有几个大于的就有几个方案了!!

- 咦? 那么如何去存储当前位置之前宽度小于当前宽度的个数呢?
    - 最简单的直接从开始到当前求和, 但是复杂度太高了
    - 因为我们需要去记录当前遍历到的宽度, 以便后续的更新, 所以我们的数据结构还需要支持更新操作
    - 那么树状数组就最适合了, 我们可以把树状数组的下标作为之前出现的宽度, 那么当前位置之前的所有和就是所有宽度比自己小的数量
    - 因为要从不用的颜色转移过来, 就需要三个不同的数组来存已经出现过的宽度
'''

# 先弄树状数组 ->
'''
init => 初始化当前树状数组
lowbit(x)
add(w) => 把当前下标为w的树状数组+1, 表示已经出现了一次
query => 查询当前位置之前有几个宽度小于自己的矩形
'''

class TreeArray():
    # 初始化
    def __init__(self, l):
        self.data = [0] * l
        # 树状数组的下标要从1开始

    # lowbit(x)
    def lowbit(self, x):
        return x & (-x)

    # add(w)
    def add(self, w):
        # 树状数组的更新操作
        while w <= MAX:
            self.data[w] += 1
            w += self.lowbit(w)

    # query
    def query(self, w):
        # 查询当前宽度之前有多少个已经遍历过的矩形
        s = 0
        while w > 0:
            s += self.data[w]
            w -= self.lowbit(w)
        return s

# 全局变量
res = 0 # 答案
MAX = 100001
MOD = int(1e9 + 7)
# 三个颜色的树状数组
T_r = TreeArray(MAX) # 红色
T_y = TreeArray(MAX) # 黄色
T_b = TreeArray(MAX) # 蓝色


# 输入
n = int(input())
info = [list(map(int, input().split())) for i in range(n)]
##print(*info)

# 按照矩形的长来降序排序
info.sort(key = lambda x : (x[0], x[1]), reverse = True)
##print("===")
##print(*info)

# 直接遍历
for a in info:
    l, w, c = a
    if c == 0: # 如果当前是红色, 那就和蓝色和黄色的转移过来
        res = (res + T_y.query(w - 1) + T_b.query(w - 1)) % MOD
        # 更新
        T_r.add(w)
    elif c == 1: # 如果当前是黄色, 那就和蓝色和红色的转移过来
        res = (res + T_b.query(w - 1) + T_r.query(w - 1)) % MOD
        # 更新
        T_y.add(w)
    if c == 2: # 如果当前是蓝色, 那就和红色和黄色的转移过来
        res = (res + T_y.query(w - 1) + T_r.query(w - 1)) % MOD
        # 更新
        T_b.add(w)
    

print(res)
