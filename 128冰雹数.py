import os
import sys

# 请在此输入您的代码

n = int(input())
ans = []
# a = []
# for i in range(2,n+1):
#     if i % 2 == 0:
#         pass
maxnum = 0


for i in range(2,n+1):
    n_inital = i - 1 
    if i % 2 == 0:
        continue
    else:
        while i != 1 and i > n_inital:
            if i > maxnum:
                maxnum = i
            if i % 2 == 0:
                i //= 2
            else:
                i = i * 3 + 1    
    
      
print(maxnum)

# AC
    