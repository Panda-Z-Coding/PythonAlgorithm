# 把字符串当做一个数字，数字相同表示字符串相同
#? 进制转换 + 求余
#? 进制是多少就根据题目定
'''
字符串哈希通过哈希函数将任意长度字符串映射为整数哈希值，
使得相同字符串生成的哈希值相同，不同字符串尽可能避免碰撞。
过预计算哈希值可实现O(1)时间复杂度的字符串比较

比如说 对于"abc" 我们进行字符串哈希转换, 我们可以用 *多项式滚动哈希* 
-  hash = (a × base^2) + (b × base^1) + (c × base^0)
这个base就是我们所说的进制数 

base为选择的基数（常取质数如31、127、131等），也就是2的次方加减1
计算结果再对一个大质数（如1e9+7）取模
'''

#! 进制转换的代码
bash = 131
def Hash(s, mod = int(1e9 + 7)):
    res = 0
    for c in s:
        res = res * bash + ord(c) - ord('A') # 从高位算到低位
        res %= mod
    return res


t = input()
s = input()
m, n = len(t), len(s)

B = 131
mod = int(1e9 + 7)
hash = [0] * (n + 1) #? 哈希前缀,所有前缀的哈希值

for i in range(1, n + 1): # 从1开始
    hash[i] = hash[i-1] * B + ord(s[i-1]) - ord('A')
    hash[i] %= mod
ans = 0 
numT = Hash(t)
p = (B ** m) % mod
# 枚举s的所有区间，看是否等于numT
for l in range(1, n + 1):
    r = l + m - 1
    if r > n:
        break
    # 求s[l...r]的哈希值 = hash[r] - hash[l - 1] * (B ** m)
    if (hash[r] - hash[l - 1] * p % mod + mod) % mod == numT:
        # +mod 为了保证是正数
        ans += 1
print(ans)