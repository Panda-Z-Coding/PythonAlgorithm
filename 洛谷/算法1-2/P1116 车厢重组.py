# 排序的最少交换次数

# 相邻两节车厢的位置交换

n = int(input())
a = []

while len(a) < n:
    num = input().strip().split() # 这里就是做到一行一行输入了
    nums = [int(i) for i in num]
    for i in nums:
        a.append(i)
    
# 从当前位置向前计算有多少个比它大的数字
cnt = 0
for i in range(n):
    for j in range(i):
        if a[j] > a[i]:
            cnt += 1
print(cnt)

# 因为只能相邻的元素交换，所以我们在交换后面的
# 元素到它应该去的位置时不会改变前面已经
# 排序好的序列
