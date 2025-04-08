n = int(input())
line = set()
nodes = set()
ans = 1

def calc(a, b):
    nodes.clear()
    for j in line:
        A = j[0]
        B = j[1]
        if A == a: #? 和当前直线平行的话, 不会和当前的直线相交
            # 是同一条直线
            continue
        x = (B - b) / (a - A)
        y = x * a + b
        nodes.add((x, y)) # 相交的点
    return len(nodes) + 1


for i in range(n):
    a, b = map(int, input().split())
    if (a, b) in line:
        continue
    ans += calc(a, b)
    line.add((a, b)) # 存储已经处理的直线

print(ans)
