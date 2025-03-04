# Next 数组

Next = [0] * 1000010
def get_next(t):
    for i in range(len(t)):
        j = Next[i]
        while j > 0 and t[i] != t[j]:
            j = Next[i]
        if t[i] == t[j]:
            Next[i + 1] = j + 1
        else:
            Next[i + 1] = 0 # 因为是自己和自己匹配

# 返回s中t出现的次数
def kmp(s, t):
    get_next(t)
    ans = 0
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != t[j]:
            j = Next[j] # 回退
        if s[i] == t[j]:
            j += 1
        # 判断是不是匹配完成
        if j == len(t):
            ans += 1
            # 回退,继续匹配
            j = Next[j]

    return ans

s = input()
t = input()
print(kmp(s, t))
        
            
        
