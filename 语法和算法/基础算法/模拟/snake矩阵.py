'''
1   2  6  7 
3   5  8 13
4   9 12 14 
10 11 15 16
'''
n,m = map(int,input().split())
k = 0
l = k + 1
value = 1
Map = []
for i in range(n+m-1):
    if k <= (n+m-1) // 2:
        if k % 2 == 0: 
            #如果k是偶数列，那么从左向右加
            Map.append([_ + value for _ in range(l)])
            value += l
            k += 1
            l = k + 1
        else:
            #从右向左减
            value += l - 1 
            Map.append([value - _ for _ in range(l)])
            k += 1
            l = k + 1
            value += 1
    else:
        if k % 2 == 0:
            l -= 2 
            #如果k是偶数列，那么从左向右加
            Map.append([_ + value for _ in range(l)])
            value += l
            k += 1
            l += 1 # 这里多加了一次，所以下次要 -2
            
        else:
            #从右向左减
            l -= 2 #
            value += l - 1 
            Map.append([value - _ for _ in range(l)])
            k += 1
            value += 1
            l += 1
k = 0
# pop(-1)组合到新数组里面
ans = [[] for _ in range(m)]
for i in range(m):
    for j in range(m):
        if (j + i) < len(Map):
            if Map[j + i]:  # 确保 Map[j + i] 不为空
                ans[i].append(Map[j + i].pop(-1))
            else:
                ans[i].append(0)  # 或者其他默认值，根据需求调整
        else:
            ans[i].append(0)  # 或者其他默认值，根据需求调整
for i in ans:
    print(" ".join(map(str, i)))