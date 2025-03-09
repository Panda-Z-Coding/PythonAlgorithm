# 表演队【算法赛】

n, k = map(int ,input().split())

val = list(map(int, input().split()))

val.sort()
ans = float('inf')
for l in range(n):
    r = l + k - 1
    if r > n - 1:
        break
    s = 0
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            s += val[j] - val[i]
    ans = min(s, ans)
print(ans)
    
