### 习题：机器人路径最大得分

**问题描述**  
机器人从 `n` 行 `m` 列的网格左上角 `(0, 0)` 出发，每一步只能向右或向下移动，最终到达右下角 `(n-1, m-1)`。每个格子中的数字表示该位置的得分，机器人经过时会累加该得分。**注意，起点和终点的得分只计算一次**。每次机器人改变移动方向（例如，上一步向右，当前步向下，或相反），会扣除 `k` 点分数。首次移动没有方向变化，因此不会扣分。求机器人能够获得的最大总得分。

---

**输入格式**  
- 第一行三个整数 `n`, `m`, `k`，表示网格的行数、列数和每次方向改变的扣分。
- 接下来 `n` 行，每行 `m` 个整数，表示每个格子的得分。

**输出格式**  
- 输出一个整数，表示最大总得分。

---

**示例输入**  
```
2 3 2
1 3 5
2 4 6
```

**示例输出**  
```
17
```

**解释**  
路径为 `右→右→下`，总得分 `1+3+5+4+6=19`。方向变化 `1` 次（右→下），扣除 `2` 分，最终得分 `19-2=17`。

---

### 解答思路  
使用三维动态规划数组 `dp[i][j][d]`，其中：
- `i` 和 `j` 表示当前位置。
- `d` 表示移动方向（`0` 为向右，`1` 为向下）。

**状态转移**：
- **保持方向**：从同一方向转移时，不扣分。
- **改变方向**：从不同方向转移时，扣除 `k` 分。

**边界条件**：
- 初始化第一步的两种可能方向（向右或向下），并累加起点和第一个移动位置的得分。

---

### 参考代码  
```python
n, m, k = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

INF = -float('inf')
dp = [[[INF] * 2 for _ in range(m)] for __ in range(n)]

# 初始化第一步
if m > 1:
    dp[0][1][0] = grid[0][0] + grid[0][1]
if n > 1:
    dp[1][0][1] = grid[0][0] + grid[1][0]

for i in range(n):
    for j in range(m):
        # 向右移动的情况（来自左侧）
        if j > 0:
            # 前一步也是向右
            if dp[i][j-1][0] != INF:
                current = dp[i][j-1][0] + grid[i][j]
                dp[i][j][0] = max(dp[i][j][0], current)
            # 前一步是向下，方向改变
            if dp[i][j-1][1] != INF:
                current = dp[i][j-1][1] + grid[i][j] - k
                dp[i][j][0] = max(dp[i][j][0], current)
        # 向下移动的情况（来自上方）
        if i > 0:
            # 前一步也是向下
            if dp[i-1][j][1] != INF:
                current = dp[i-1][j][1] + grid[i][j]
                dp[i][j][1] = max(dp[i][j][1], current)
            # 前一步是向右，方向改变
            if dp[i-1][j][0] != INF:
                current = dp[i-1][j][0] + grid[i][j] - k
                dp[i][j][1] = max(dp[i][j][1], current)

max_score = max(dp[n-1][m-1][0], dp[n-1][m-1][1])
print(max_score)
```

---

**关键点**  
- **状态设计**：通过三维状态 `dp[i][j][d]` 跟踪当前位置和方向。
- **方向变化处理**：在状态转移时判断是否需要扣除 `k` 分。
- **边界处理**：初始化第一步的两种情况（向右或向下），确保起点得分被正确累加。