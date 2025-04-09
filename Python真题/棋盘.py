N = 2009
d = [[0] * N for i in range(N)]
n, m = map(int, input().split())

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    d[x1-1][y1-1] += 1
    d[x1-1][y2] -= 1
    d[x2][y1-1] -= 1
    d[x2][y2] += 1
# 下标从1开始！要不然会出现负坐标, 就会发生错误    

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 求二维前缀和
        d[i-1][j-1] = d[i-1][j-1] + d[i-2][j-1] + d[i-1][j-2] - d[i-2][j-2]
        if d[i-1][j-1] & 1:
            print("1", end='')
        else:
            print('0', end='')
    print()
