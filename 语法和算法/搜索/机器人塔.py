a, b = map(int, input().split())
ans = 0

def dfs(A, B, s):
    '''
    A: 剩余的A的数量
    B: 剩余的B的数量
    s: 当前的塔的构造(横向)
    '''
    
    global ans
    
    #? 递归的出口, 符合条件的方案, A == B == 0
    if A == 0 and B == 0:
        ans += 1
        return
    
    #? 剪去不可能的情况
    if A < 0 or B < 0:
        return
    
    for i in 'AB':
        # 来回尝试从A或者B开始的这一层的结果
        Str =  i
        for j in s:
            #! s是上一层的构造
            #? 这一层的for是为了把当前的所有可以出现的字符串都求出来
            if j == 'A':
                if Str[-1] == 'A':
                    '''
                    A
                    AA
                    '''    
                    Str += 'A'
                else:
                    '''
                    B
                    AB
                    '''
                    Str += 'B'
            else: # j == 'B'
                if Str[-1] == 'A':
                    '''
                    B
                    BA
                    '''
                    Str += 'B'
                else:
                    '''
                    A
                    BB
                    '''
                    Str += 'A' 
        if A - Str.count('A') >= 0 and B - Str.count('B') >= 0:
            # AB数量都有余的时候可以继续往下排列
            dfs(A - Str.count('A'), B - Str.count('B'), Str)
            
# 第一个从A排起
dfs(a-1, b, 'A')
dfs(a, b-1, 'B')

print(ans)