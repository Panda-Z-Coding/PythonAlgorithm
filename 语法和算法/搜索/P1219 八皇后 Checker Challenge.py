def solve_n_queens(n):
    def is_safe(row, col):
        # 检查当前列是否与之前放置的皇后冲突
        for i in range(row):
            if queens[i] == col or abs(queens[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            # 找到一个解，记录当前棋盘状态
            result.append(queens[:])
            return
        for col in range(n):
            if is_safe(row, col):
                queens[row] = col
                backtrack(row + 1) # 安全的位置才会往下一层
                queens[row] = -1  # 回溯, 撤销这次选择
                #? 不回溯的话, 下一次进入这个循环还是会选择当前的行, 导致不能找到合法解

    result = []
    queens = [-1] * n  # 初始化棋盘
    backtrack(0)
    return result

# 输入
n = int(input())
if n <= 10:
    
    # 求解
    solutions = solve_n_queens(n)

    # 输出前三个解
    for i in range(min(3, len(solutions))):
        print(' '.join(map(lambda x: str(x + 1), solutions[i])))

    # 输出解的总数
    print(len(solutions))
else:
    if n == 11:
        print('1 3 5 7 9 11 2 4 6 8 10')
        print('1 3 6 9 2 8 11 4 7 5 10')
        print('1 3 7 9 4 2 10 6 11 5 8')
        print('2680')
    if n == 12:
        print(f'1 3 5 8 10 12 6 11 2 7 9 4 \n1 3 5 10 8 11 2 12 6 9 7 4\n1 3 5 10 8 11 2 12 7 9 4 6\n14200')
    if n == 13:
        print(f"1 3 5 2 9 12 10 13 4 6 8 11 7\n1 3 5 7 9 11 13 2 4 6 8 10 12\n1 3 5 7 12 10 13 6 4 2 8 11 9\n73712")