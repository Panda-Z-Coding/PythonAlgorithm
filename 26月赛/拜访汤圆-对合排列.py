MOD = 10**9 + 7
max_n = 10**6

# 预处理对合排列数
a = [0] * (max_n + 1)
a[0] = 1
a[1] = 1

for i in range(2, max_n + 1):
    a[i] = (a[i-1] + (i-1) * a[i-2]) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(a[n])
