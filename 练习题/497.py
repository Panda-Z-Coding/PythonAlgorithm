import os
import sys

# 请在此输入您的代码

n = int(input())
scores = list()

for i in range(n):
    scores.append(int(input()))
    
print(max(scores))
print(min(scores))
print("{:.2f}".format(sum(scores)/n))

'''
以后四十五入用format()函数,  "{:.2f}".format(数) 
 ! round()函数,比如说3.80这种情况就会舍去0变成3.8 !
 
Python有很多内置函数要善于运用
max() # 可迭代的对象都可以
min()
"{:.2}".format()
 
'''