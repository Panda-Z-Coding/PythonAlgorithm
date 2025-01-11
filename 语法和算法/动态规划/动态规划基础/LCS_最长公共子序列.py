'''
两个数组的最长公共子序列
二维dp

状态: dp[i][j] ->  数组a前i个和数组b前j个的最长公共子序列
边界: dp[0][0] = dp[...][0] = do[0][...] = 0

dp[i][j] = {
    dp[i-1][j-1] + 1, a1[i] == a2[j]
    max(dp[i-1][j], dp[i][j-1]), other
}
'''

'''
? 如何回溯出子序列
当dp表往左上角走的时候, a1 == b1
'''

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
lenA, lenB = len(A), len(B)
dp = [[0] * (m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # dp[i][j] 表示字符串 A 的前 i 个字符和字符串 B 的前 j 个字符的最长公共子序列的长度
        # 如果 A[i-1] 和 B[j-1] 相等，那么 dp[i][j] = dp[i-1][j-1] + 1
        # 否则，dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else max(dp[i-1][j], dp[i][j-1])
print(dp[n][m])

# ans
ans = []
x, y = n, m
while x != 0 and y != 0:
    if dp[x][y] == dp[x-1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y-1]:
        y -= 1
    else:
        # 此时 A[x] == B[x]
        ans.append(A[x])
        x -= 1
        y -= 1

print(ans[::-1])