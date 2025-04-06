import os
import sys

# 2021 张 0 ~ 9
# 纯纯模拟一遍
nums = [2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021, 2021]
mod = 10
i = 1 #
while sum(nums) != 0:
    s = ''
    for d in str(i):
        if nums[int(d)] > 0: 
            s += d
            nums[int(d)] -= 1
        else:
            break
    # print(s)
    if s == str(i):
        i += 1 # 这是指最后一个符合条件的数字, 所以多加了一个1
    else:
        break

print(i - 1)
    
