# dp[i][j] 表示前i本书, 进行到了j 时间的最大含金量
# 那我要买这门课，要满足？
# 当前进行的时间大于等于这门课的等待时间，小于等于这门课的结束时间

n = int(input())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
A = [0] + sorted(A, key = lambda x: x[1])
dp = [0] * 100010

for i in range(1, n + 1):
    a, b, c = A[i]
    for j in range(b, a - 1,-1):
        dp[j] = max(dp[j], dp[j - a] + c)
print(max(dp))
