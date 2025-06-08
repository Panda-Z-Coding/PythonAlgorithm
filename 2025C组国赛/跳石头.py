import sys

input = sys.stdin.readline

n = int(input())
c = [0] + list(map(int, input().split()))

# bs[i] 表示从位置 i 能跳到的“分数值”集合（用 set 存储）
bs = [set() for _ in range(n + 2)]
ans = 0

# 从 n 到 1 遍历（自底向上 DP）
for i in range(n, 0, -1):
    # 当前能跳到的分数 c[i]
    bs[i].add(c[i])

    # 合并从 i + c[i] 跳过来的集合（如果合法）
    if i + c[i] <= n:
        bs[i].update(bs[i + c[i]])

    # 合并从 i * 2 跳过来的集合（如果合法）
    if i * 2 <= n:
        bs[i].update(bs[i * 2])

    # 更新最大分数种类数量
    ans = max(ans, len(bs[i]))

print(ans)
