# 按照元组存起来然后排个序就好了

# 之后把分数线存起来，然后不符合的排除

n, m = map(int, input().split())
a = []

for i in range(n):
    h, s = map(int, input().split())
    a.append((h, s))

# 排序
a.sort(key = lambda x: (x[1], -x[0]), reverse = True)
# print(a)

# 计算分数线

line = int(m * 1.5) - 1 # 这个下标要注意，我们是从零开始的
score = a[line][1]
# print(line)
# print(score)
a = [i for i in a if i[1] >= score]
# print(a)

print(score, len(a))

for i in a:
    print(i[0], i[1])
