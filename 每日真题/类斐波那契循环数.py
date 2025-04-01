# 也就是当前数字的每一位先存放到序列中,
# 然后每个数等于前k个数相加,
# 如果它自己本身在这序列中就是符合的

## 从第四个数开始
flag = False
ans = 0
for i in range(10000000, 1, -1): # 找最大的都可以倒序遍历
     if flag: break
     a = [int(ch) for ch in str(i)] # 简便的获取每一位数字
     
     sum1 = 0
     while True:
         sum1 = sum(a)
         if sum1 < i:
            a.append(sum1)
            a.pop(0) # 用完就扔
         elif sum1 == i:
            flag = True
            ans = i
            break
         else: # 剪枝
            break
print(ans)

