import os
import sys

# 请在此输入您的代码

n = int(input())
scores = []
for i in range(n):
    j = int(input())
    scores.append(j)
l = len(scores)
Pass_rate = 0
Nice_rate = 0
sum = 0
for score in scores:
    if int(score) >= 60:
        sum += 1
    Pass_rate = round((sum / l) * 100)
sum = 0 
for score in scores:
    if int(score) >= 85:
        sum += 1
    Nice_rate = round((sum / l) * 100)
    
print(str(Pass_rate) + '%')
print(str(Nice_rate) + '%',end='')