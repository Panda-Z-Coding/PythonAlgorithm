import os
import sys
input = sys.stdin.readline

'''
# 先要搞懂这个左括号是和谁匹配的

s = input().strip()
q = int(input())
# print(s)

def query(c, x):
    # 查询
    ans = 0
    for li in mp.values():
        if li.count(c) >= x:
            ans += 1
    return ans
        


# 利用栈来分析所有匹配的括号对下标
stack = []  # ('c', idx)
char = [] # ('c', idx) # 用于存储字母和下标
mp = {}
for idx, c in enumerate(s):
    # 先入栈
    # 如果是字母就不入栈
    if c != '(' and c != ')':
        char.append((c, idx))
        continue
    
    # 如果当前处理的是 '(' 就入栈
    if c == '(':
        stack.append((c, idx))
    else:
        # 从当前的栈出栈一个进行匹配
        cc, idxx = stack.pop()
        mp[(idxx, idx)] = []
    # print(stack)
    # print(1)
# print(char)
# print(mp) 没问题

# 之后就是遍历所有的括号范围然后更新进来
for c, idx in char:
    # 遍历字典
    for l, r in mp.keys():
        if l <= idx <= r:
            mp[(l, r)].append(c)

# print(mp) 大功告成

for _ in range(q):
    c, x = input().split()
    x = int(x)
    # query
    print(query(c, x))
    
# 40 % 
# 这种解法太暴力了
# 我们用栈去获取匹配的括号下标是妹问题的
# 只不过后面的判断太费时间了
# 这里我们可以新学到一个 => 字符串前缀和 => prefix['c'][i] :: c这个字符串在 0, ... , i - 1 出现了多少次 
'''





