# 2.酒店安排

n, m = map(int, input().split()) # n是酒店的数量，m是人数
loc = list(map(int, input().split()))

'''
就是任意的子集的差值的最小值
'''

# 先排序
loc.sort()
ans = float('inf')
# 1 3 4 5 6
for i in range(n):
    if i + m > n:
        break
    ans = min(ans, loc[i:i + m][-1] - loc[i:i + m][0])
print(ans)
