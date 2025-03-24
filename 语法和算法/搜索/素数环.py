import sys
input = sys.stdin.readline

# 线性筛
def get_prime(x):
    # 获得从2 - x的素数列表
    prime = []
    vis = [0] * (x + 1)
    vis[0] = vis[1] = 1
    for i in range(2, x + 1):
        if vis[i] == 0:
            prime.append(i)
        for now_prime in prime:
            if now_prime * i > x: break
            vis[i * now_prime] = 1
            if i % now_prime == 0: break
    return prime

# 回溯法
def dfs(i):
    # i表示当前要处理的下标位置
    
    # 出口
    if i == n and cur_prime[-1] + cur_prime[0] in prime:
        ans.append(cur_prime[:])
        return 
    
    # 扩展
    for num in prime:
        # 要满足当前一个和前一个相加也是素数 => prime[i-1] + x = num
        #? x表示当前要存放的数字, 从小到大枚举的素数也能保证答案是从小到大的
        x = num - cur_prime[i-1]
        if 1 <= x <= n and not vis[x]:
            # 插旗
            vis[x] = 1
            cur_prime.append(x)
            # 下一层
            dfs(i + 1)
            # 回溯
            vis[x] = 0
            cur_prime.pop()




n = int(input())

vis = [0] * (n + 1) # 标记数字有没有出现过
cur_prime = [1] # 用于存储当前的答案序列
prime = get_prime(n << 1)
print(*prime)
ans = []
vis[1] = 1
dfs(1)

for i in ans:
    print(*i)