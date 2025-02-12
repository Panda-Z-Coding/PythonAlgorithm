n = int(input())

a = []
for i in range(n):
    a.append(int(input()))
a_sum = sum(a)
if a_sum % 2 == 1:
    print('no')
else:
    dp = [0] * (a_sum // 2 + 1)
    for k in a:
        for j in range(a_sum // 2, k-1, -1):
            dp[j] = max(dp[j], dp[j - k] + k)
    print("yes" if dp[a_sum // 2] == a_sum // 2 else "no")
