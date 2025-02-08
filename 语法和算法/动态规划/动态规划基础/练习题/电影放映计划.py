'''
思考🤔? 有放映时间也就是背包的容量，有利润也就是价值，还有一个间隔，这个是最主要的
那这个间隔，每次我们排进一部电影，在加上当前电影的时间再加上k

状态: dp[i][j] -> 前i部电影时间为j的最大价值

'''

m, n = map(int, input().split())
Movie = []

for i in range(n):
    Movie.append(list(map(int, input().split()))) # 0 -> 时长 # 1 -> 利润
k = int(input())
for i in range(n):
    Movie[i][0] += k
m += k
dp = [0] * (m + 1)
for i in range(n):
    wi, vi = Movie[i][0], Movie[i][1]

    for j in range(1, m + 1):
        if wi <= j:
            dp[j] = max(dp[j], dp[j - wi] + vi)
print(dp[m])