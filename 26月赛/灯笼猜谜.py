n, m = map(int, input().split())
pos = []
for i in range(n):
    pos.append(list(map(int, input().split())))

# 表示灯笼位置，从1开始
long = [0 for i in range(n + 1)]

# 有三种情况
# 1. 当前手在下一个谜语左边，那就取下一个的左边作为下一个的落点
# 2. 当前手在下一个谜语右边, 那就取下一个的右边作为下一个的落点
# 3. 当前手在下一个谜语中, 不动, Continue
cur_pos = 1 # 当前手的位置
tired = 0 
for l, r in pos:
    if cur_pos < l:
        tired += l - cur_pos
        cur_pos = l
    elif cur_pos > r:
        tired += cur_pos - r
        cur_pos = r
    else:
        continue
print(tired)
