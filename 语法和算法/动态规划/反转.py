import os
import sys
input = sys.stdin.readline
# 长度我2的字符串
# 按顺序
# 因为每次的长度大小都只和前一个字符串反转与否有关系，而且又是按照顺序来拼接的
# so，我们用字典存储以c为结尾的字符串的长度就可以了，然后for循环遍历

n = int(input())
parts = [input().strip() for _ in range(n)]

# dp[i][c] 表示前i个工件，最后一个字符是c时的最小长度
# 初始时，i=0，没有工件，长度为0，没有最后一个字符（可以认为不影响）
# 用两个字典：prev_dp 和 current_dp
prev_dp = {} # {'char': len}
# 初始状态：处理第0个工件（无工件），长度为0，最后一个字符可以认为是None，但无法合并
# 但为了统一，可以认为初始时没有限制，长度为0
prev_dp[None] = 0

for i in range(n):
    s = parts[i]
    current_dp = {}
    # 不翻转
    a, b = s[0], s[1]
    for last_char in prev_dp: # 这个for就是反转前面一个字符串的意思了
        if last_char == a:
            new_len = prev_dp[last_char] + 1
        else:
            new_len = prev_dp[last_char] + 2
        if b in current_dp:
            if new_len < current_dp[b]:
                current_dp[b] = new_len
        else:
            current_dp[b] = new_len
    # 翻转
    a, b = s[1], s[0]
    for last_char in prev_dp:
        if last_char == a:
            new_len = prev_dp[last_char] + 1
        else:
            new_len = prev_dp[last_char] + 2
        if b in current_dp:
            if new_len < current_dp[b]:
                current_dp[b] = new_len
        else:
            current_dp[b] = new_len
    prev_dp = current_dp # 这里更新，存储上一个位置的dp
    # print(prev_dp)

print(min(prev_dp.values()))


