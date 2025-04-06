import os
import sys
input = sys.stdin.readline
# 输入
from collections import Counter
s = list(input().strip())

s = Counter(s)
cnt = 0
max_s = 'a'
for ss, i in s.items():
    if cnt < i:
        cnt = i
        max_s = ss

print(max_s)
print(cnt)

