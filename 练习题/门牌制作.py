import os
import sys
from collections import Counter
# 数出现2的次数

cnt = 0
for i in range(1, 2021):
    c = Counter(str(i))
    # print(c)
    cnt += c['2']
print(cnt)
