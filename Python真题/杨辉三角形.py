import sys
input = sys.stdin.readline

n = int(input())

def C(a, b):
    res = 1
    j = 1
    i = a
    while j <= b:
        res = int(res * i / j)
        if res > n:
            return int(res)
        i -= 1
        j += 1
    return int(res)


for k in range(16, -1, -1):
    # 从大到小枚举列
    l = 2 * k # 开始有效的行
    r = max(n, l)
    res = int(-1)
    while l <= r:
        # 二分搜索行
        mid = l + r >> 1
        if C(mid, k) >= n:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    if C(res, k) == n: # 如果找到了
        print((res + 1) * res // 2 + k + 1)
        break




