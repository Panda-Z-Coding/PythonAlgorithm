import os
import sys

# 状态压缩

score = [5, 5, 10, 10, 15, 15, 20, 20,25, 25] # 10
st = set()
for mask in range(1 << 10):
    total = 0
    for i in range(10):
        # 每一个进行比对
        if mask & (1 << i): # mask & (1 << i) 表示当前这一位是有的
            total += score[i]
    st.add(total)

print(len(st))


