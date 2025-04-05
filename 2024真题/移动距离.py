import os
import sys

# 请在此输入您的代码
def get_coordinate(w, num):
    """计算楼号对应的行号和列号"""
    row = (num - 1) // w + 1  # 行号,从1开始
    col = (num - 1) % w + 1   # 列号,从1开始
    if row % 2 == 0:  # 如果行号为偶数，列号从右到左递减
        col = w - col + 1
    return row, col

def min_distance(w, m, n):
    """计算两个楼号之间的最短移动距离"""
    row_m, col_m = get_coordinate(w, m)
    row_n, col_n = get_coordinate(w, n)
    return abs(row_m - row_n) + abs(col_m - col_n)

# 输入处理
w, m, n = map(int, input().split())

# 输出结果
print(min_distance(w, m, n))
