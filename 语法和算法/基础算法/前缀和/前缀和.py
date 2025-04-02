""" 前缀和:
    这个下标的前面所有相加
    sum[i] = sum[i - 1] + a[i]

    这样的好处就是不用在for循环遍历就可以求出区间长度

    form itertools import accumulate

    sum = list(accumulate(a)) #也可以
"""
from itertools import accumulate # 直接用库函数也行

def get_presum(arr):#下标从0开始
    n = len(arr)
    sum = [0] * n
    sum[0] = arr[0]
    for i in range(1,n):
        sum[i] = sum[i-1] + arr[i]
    return sum

# 求区间[l,r]的和
# a[l]+...+a[r] = sum[r] - sum[l-1]

def get_sum(sum,l,r):
    if l == 0:
        return sum[r]
    else:
        return sum[r] - sum[l - 1]

def get_presum1(arr):
    n = len(arr)
    sum = [0] * n
    sum[0] = arr[0]
    for i in range(1, n):
        sum[i] += sum[i-1] + arr[i]
    return sum

def get_sum1(sum, l, r):
    return sum[r] if l == 0 else sum[r] - sum[l - 1]

 


a = [1,2,3,4,5,6,7]
sum = get_presum1(a)
print(a)
print(sum)
print(get_sum1(sum,0,4))