from numpy import diff


def output(a, n):
    for i in range(1,n+1):
        print(' '.join(map(str, a[i][1:])))
        
#? 创建二维前缀和
def get_sum_td(arr):
    presum_td = [[0] * (m + 1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            presum_td[i][j] = presum_td[i-1][j] + presum_td[i][j-1] - presum_td[i-1][j-1] + arr[i][j]
    return presum_td

#? 二维差分
def get_diff_td(arr):
    diff_td = [[0] * (m + 1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            diff_td[i][j] = arr[i][j] - arr[i-1][j] - arr[i][j-1] + arr[i-1][j-1]
    return diff_td

#? x1y1 到 x2y2 的和
def get_sum_x1y1_x2y2(sum_, x1, y1, x2, y2):
    return sum_[x2][y2] - sum_[x1 - 1][y2] - sum_[x2][y1 - 1] + sum_[x1 - 1][y1 - 1]  

n, m= map(int, input().split())

#下标1开始
# a = [[0] * (m + 1) for i in range(n+1)]
arr = [[0] * (m + 1) for i in range(n+1)]

for i in range(1,n+1):
    arr[i] = [0] + list(map(int, input().split()))
    
# print("=========")
# output(a, n)
# print("=========")

a = get_sum_td(arr)
b = get_diff_td(arr)
# output(presum_td, n)
# ans = 0
# #枚举左上角
# for x1 in range(1, n+1):
#     #宽 -> m
#     for y1 in range(1, m+1):
#         #枚举右下角
#         for x2 in range(x1,n+1):
#             for y2 in range(y1,m+1):
#                 if get_sum_x1y1_x2y2(a, x1, y1, x2, y2) <= k:
#                     ans += 1
print()
output(a,n)
print()
output(b,n)