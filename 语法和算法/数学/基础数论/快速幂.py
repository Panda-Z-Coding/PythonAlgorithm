def ksm(a, b, c):
    #? 求解 a ^ b % c
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    ans = ksm(a, b // 2, c) # 递归分解求
    ans = ans * ans % c
    if b % 2 == 1: #? 其实就是 2k + 1 分解为 2k 和 1, 我们把那个1补上就行了s
        ans = ans * a % c
    return ans

def ksm_pro(a, b, c):
    ans = 1
    a = a % c  # 预处理，减少后续计算量
    while b > 0:
        if b & 1:  # 如果b的当前最低位是1
            ans = ans * a % c
        a = a * a % c  # 平方
        b >>= 1  # 右移一位，相当于除以2
    return ans


print(ksm_pro(2, 10, 10000007))



def ksm(a, b, c):
    ans = 1
    a %= c
    while b > 0:
        if b & 1: # 如果是奇数, 就乘上a
            ans = ans * a % c
        a = a * a % c
        # 平方
        b >>= 1
    return ans