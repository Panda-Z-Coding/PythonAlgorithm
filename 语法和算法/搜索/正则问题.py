'''
( => 表示要进入一层dfs去算这个括号里面所能接受的最长字符串长度
) => 表示这一层dfs结束了，要返回最长的长度
| => 表示前面的答案要清零，pos+1，去下一个字符串算长度
x => 碰到x就长度+1

用一个pos全局变量来追踪当前位置
ans 表示当前dfs层的最长字符串长度
temp 表示没遇到 | 的字符串长度

有下面几种操作
1. (
    pos+1跳过，然后进入(的层，ans+=dfs()
2. )
    pos+1跳过，然后返回当前最长的字符串长度
3. |
    ans = max(ans, temp)
    temp = 0
4. x
    temp += 1
'''
pos = 0
S = input()
S_len = len(S)
def dfs():
    global pos
    ans, temp = 0, 0
    while pos < S_len:
        if S[pos] == '(':
            pos += 1
            ans += dfs()
        elif S[pos] == '|':
            pos += 1
            ans = max(ans, temp)
            temp = 0
        elif S[pos] == 'x':
            pos += 1
            temp += 1
        elif S[pos] == ')':
            pos += 1
            ans = max(ans, temp)
            return ans
        ans = max(ans, temp)
    return ans

print(dfs())
