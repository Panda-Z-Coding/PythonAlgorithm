# 贪心的策略:
# 先把所有正面小于背面的卡牌先翻转过来(其实就是存入一个列表里面)进行降序排序，之后取前面k个即可，先算出其余的正面的数字和
# 那我们就用三元组来给每一个牌多一个信息，前k个被选择翻牌的就标记True

n, k = map(int, input().split())
a = list(map(int, input().split())) # 正面
b = list(map(int, input().split()))# 背面

# 组合成三元组
cards = []
for i in range(n):
    cards.append([a[i], b[i], False])
# print(cards)
pre = []
# 把所有背面大于正面的卡牌(背面数字, 下标)存进pre
for i in range(n):
    if cards[i][0] < cards[i][1]:
        pre.append((cards[i][1], i))

pre.sort(key = lambda x: x[0], reverse = True)

for i in range(min(k, len(pre))):
    # 取前面k个
    cards[pre[i][1]][2] = True

# print(cards)

sum_ = 0
for i in cards:
    if i[2]:
        sum_ += i[1]
    else:
        sum_ += i[0]

print(sum_)
# ---------------这个贪心策略是错的, 不完全对, 有的时候正面小于背面要进行翻转才能达到最大, 所以我们要求出背面和正面的差值

diff = [b[i] - a[i] for i in range(n)]
diff.sort(reverse=True)

total = sum(a) # 先求不翻转任何卡牌的和, 再加上前min(k, len(diff))个差值大于0的
for i in range(min(k, n)):
    if diff[i] > 0:
        total += diff[i]
print(total)