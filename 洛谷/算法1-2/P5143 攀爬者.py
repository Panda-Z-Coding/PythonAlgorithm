# 按照z轴来排序，从小到大

n = int(input())
a = []
for i in range(n):
    x, y, z = map(int, input().split())
    a.append((x, y, z))

a.sort(key = lambda x: x[2])

s = 0
for i in range(1, n):
    s += ((a[i][0] - a[i-1][0]) ** 2 + (a[i][1] - a[i-1][1]) ** 2 + (a[i][2] - a[i-1][2]) ** 2) ** 0.5

print(f"{s:.3f}")
    
