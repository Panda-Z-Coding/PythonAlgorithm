"""
建树
"""
def tree(n):
    tree_ = []
    pre = 1
    for i in range(n):
        for j in range(pre):
            tree_.append(j+1)
        pre *= 2
    return tree_

def look_for(p_) -> int:
    #p_是一个字符串
    dir = 0 # 下标
    for p in p_:
        if p == 'L':
            dir = 2*dir + 1
        if p == 'R':
            dir = 2*dir + 2
    return dir
            

n, q = map(int, input().split())   
tr = tree(n)
ans = []
for i in range(q):
    s = input()
    ans.append(tr[look_for(s)])
    
print("\n".join(map(str, ans)))
    