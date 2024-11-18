"""
求区间次方和
"""
MOD  = 1000000007
def get_presum(arr): # 从0开始
    l = len(arr)
    sum = [0] * l
    sum[0] = arr[0]
    for i  in range(l):
        sum[i] = (sum[i-1] + arr[i]) % MOD
    return sum

def get_sum(sum, l, r):
    if l == 0:
        return sum[r]
    else:
        return (sum[r] -sum[l-1] + MOD) % MOD

#存储a数组的前缀和、a数组平方的前缀和。。。
sum_list = []


n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1,6):
    sum_list.append(get_presum([x ** i for x in a]))
    #求每个k的前缀和，因为k固定就5个


for _ in range(m):
    l, r, k = map(int,input().split())
    print(get_sum(sum_list[k-1], l-1, r-1))