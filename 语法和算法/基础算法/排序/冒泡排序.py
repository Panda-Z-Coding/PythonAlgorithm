'''
长度为n的,要循环n-1次
'''
n = int(input())
a = list(map(int, input().split()))


# 循环n-1次，每次获得第i大的数字
for i in range(1, n - 1):
    # 每次比较a[j] 和 a[j + 1]
    for j in range(0, n - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1] + a[j]
print(a)  