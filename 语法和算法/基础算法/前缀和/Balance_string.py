"""
最长平衡字符串

    ！区间的统计都可以转换为前缀和问题！
"""
#构建前缀和,下标0开始
from itertools import accumulate

def get_sum(sum, l, r):
    if l == 0:
        return sum[r]
    else:
        return sum[r] - sum[l-1]
    

#数据输入
str_ = input()
n = len(str_)
#print(str_)
#L为+1，Q为-1，这样就求区间和为0的最长区间
#枚举所有区间
ba_str = []
for s in str_:
    if s == 'L':
        ba_str.append(1)
    else:
        ba_str.append(-1)
#print(ba_str)
ba_sum = list(accumulate(ba_str))
del ba_str
del str_
ans = 0
for l in range(n):
    for r in range(l, n):
        if get_sum(ba_sum, l, r) == 0:
            ans = max(ans, r - l + 1) # 1 2 这个下标区间的长度是2-1+1
print(ans)
            
