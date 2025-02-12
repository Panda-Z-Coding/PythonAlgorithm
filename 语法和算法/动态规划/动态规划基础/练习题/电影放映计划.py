'''
思考🤔? 我们要注意, 并没有说每一部电影都只能放映一次, 所以这是一个完全背包问题
那么我们就要终点处理间隔的问题, 每一个电影都加上k, 但是第一个放映的不用间隔, 所以
在后续的m总时间加回去

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