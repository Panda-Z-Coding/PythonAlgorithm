# 在埃氏筛中, 同一个合数会别很多个质因数筛

def f(n):
    '''
    - 从 2~n 遍历, 查看i是否被筛, 没有就是质数
        - now_prime => 当前的质数列表
            - 如果 i * now_prime > n: break
            - 每次筛 i * now_prime 
            - 如果 i 是 now_prime 的倍数则停止
    '''
    prime = []
    vis = [0] * (n + 1)
    vis[0] = vis[1] = 1
    for i in range(2, n + 1):
        if vis[i] == 0:
            prime.append(i)
        # 遍历当前的质数列表
        for now_prime in prime:
            if i * now_prime > n: break
            # 筛除 i * now_prime
            vis[i * now_prime] = 1
            if i % now_prime == 0: break #? 这是为了保证每个合数只被最小的质因子筛
    return prime
#! O(n)

print(*f(16))