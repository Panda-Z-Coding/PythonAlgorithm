def find_min_B(arr):
    # 统计所有 A[i] 的二进制表示中出现的 1
    mask = 0
    for num in arr:
        mask |= num
    # 找到最小的 B，其二进制表示中不包含 mask 中的 1
    B = 1
    while (B & mask) != 0:
        B += 1
    return B
# 输入处理
n = int(input())
arr = list(map(int, input().split()))
# 计算最小 B
min_B = find_min_B(arr)
# 输出结果
print(min_B)

#? A + B = A ^ B <==> A & B = 0
#? A + B 会产生进位, A ^ B 如果要和 A + B相同的话不能让A + B产生进位
#? 加法产生不进位的话, A ^ B 就能和 A + B相等
#? 4 = 0100 ^ 0011 = 3 <==> 0100 + 0011 = 0111 = 0100 ^ 0011 = 0111 