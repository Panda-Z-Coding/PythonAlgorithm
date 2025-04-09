import os
import sys
import math
def lcm(a, b):
    return a * b // math.gcd(a, b)
# 这个数是187的倍数
L = []
for i in range(187000000,10**12,187):
     if i%44==33 and i%45==29 and i%46==15 and i%47==5 and i%48==41 and i%49==46:
     #else:
         L.append(i)
     if len(L)>=2:
         break
step = L[1] - L[0]
for i in range(L[0],10**17,step):
    if i%20==9 and i%25==9 and i%26==23 and i%27==20 and i%28==25 and i%29==16 and i%30==29 and i%31==27 and i%32==25 and i%33==11 and i%34==17 and i%35==4 and i%36==29 and i%37==22 and i%38==37 and i%39==23 and i%40==9 and i%41==1 and i%42==11 and i%43==11 :
        print(i)
        break
