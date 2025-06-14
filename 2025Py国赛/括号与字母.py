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


import bisect
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    s = data[0]
    ptr = 1
    q = int(data[ptr])
    ptr += 1
    queries = []
    for _ in range(q):
        c = data[ptr]
        x = int(data[ptr+1])
        queries.append((ord(c)-ord('a'), x))
        ptr += 2

    # 1. 括号匹配预处理
    stack = []
    brackets = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            l = stack.pop()
            brackets.append((l, i))
    brackets.sort()

    # 2. 构建前缀和数组
    n = len(s)
    prefix = [[0]*(n+1) for _ in range(26)]
    for i in range(n):
        ch = s[i]
        if ch.isalpha():
            idx = ord(ch) - ord('a')
            for c in range(26):
                prefix[c][i+1] = prefix[c][i] + (1 if c == idx else 0)
        else:
            for c in range(26):
                prefix[c][i+1] = prefix[c][i]

    # 3. 预处理字符计数
    char_counts = defaultdict(list)
    for l, r in brackets:
        for c in range(26):
            cnt = prefix[c][r+1] - prefix[c][l]
            if cnt > 0:
                char_counts[c].append(cnt)
    for c in char_counts:
        char_counts[c].sort()

    # 4. 处理查询
    results = []
    for c, x in queries:
        if x == 0:
            results.append(len(brackets))
        else:
            lst = char_counts.get(c, [])
            pos = bisect.bisect_left(lst, x)
            results.append(len(lst) - pos)
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()



