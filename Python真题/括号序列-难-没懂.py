import sys
input = sys.stdin.readline

S = input().strip()
n = len(S)
mod = 1000000007
N = n + 5

def calc():
    dp = [[0] * N for i in range(N)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        if S[i - 1] == '(':
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] % mod
        else:
            dp[i][0] = (dp[i-1][1] + dp[i-1][0]) % mod
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j + 1] + dp[i][j - 1]) % mod
    for i in range(0, n + 1):
        if dp[n][i] != 0:
            return dp[n][i]

left = calc() % mod

# 反转再求一次
S = ''.join([')' if char == '(' else '(' for char in reversed(S)])
right = calc() % mod

print((left * right) % mod)



        
