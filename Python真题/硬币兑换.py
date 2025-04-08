import os
import sys

# 请在此输入您的代码
# 兑换机结果集
result=[0 for r in range(4047)]

### 要把每一个情况都考虑到
##for i in range(1,2024):
##  for j in range(i+1,2024):
##    result[i+j]+=i
##print(max(result))

for i in range(1, 2024):
    for j in range(i + 1, 2024):
        result[i + j] += i
print(max(result))
