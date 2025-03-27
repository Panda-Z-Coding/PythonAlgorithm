# 可以用前缀和先处理出每一个的值减去平均值的平方的前缀和
# 这样可以简化每次求方差的时间, 但是问题是？？
# 如何在前x个找出k个去求解方差

#?

import sys
input = sys.stdin.readline

n, k, t = map(int, input().split()) 

a = [0] + list(map(int, input().split()))
# print(a)
# 遍历b数组, 每次取k个数进行计算方差
def check(mid):
    b = a[:mid + 1]
    b.sort()
    # print(b)

    # 计算平均值，计算有误，这里算的是整个的，但是我们每次只取k个！！
    # v = sum(b) / mid
    # # print(v)
    # # 记录(b[i][0] - v)^2 的前缀和
    # pre = [0] * (mid + 1) # 1开始
    # pre[1] = (b[1] - v)*(b[1] - v)
    # for i in range(2, mid + 1):
    #     pre[i] = pre[i-1] + (b[i] - v)*(b[i] - v)
    # # print(pre)
    # for r in range(k, mid + 1):
    #     vs = pre[r] - pre[r - k]
    #     f = vs / k # 方差
    #     if f < t:
    #         # print(f)
    #         return True
    # return False

    # 正确的是要取出k个区间进行求解
    v2 = v = 0
    for i in range(1, k): # 先取前k个的和, 之后在用滑动窗口的思想取更新区间
        v2 += b[i] * b[i] # 记录平方的前缀和
        v += b[i] # 记录前缀和
    
    for i in range(k, mid + 1):
        # k个k个取
        v2 += b[i]*b[i] - b[i-k]*b[i-k]
        v += b[i] - b[i-k]
        avg = v / k
        # 使用改进的方差公式
        if (v2 - 2 * avg * v + k * avg * avg) / k < t:
            return True
    return False


        
# 二分枚举要取前mid个
l, r = k, n
res = -1
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1
        res = mid
    else:
        l = mid + 1

print(res)
