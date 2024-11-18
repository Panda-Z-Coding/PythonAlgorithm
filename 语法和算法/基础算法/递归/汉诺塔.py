def Move(n, A, B, C):
    # 将 n个数从 A柱子移到 C柱子，利用 B柱子
    # 写好逻辑就可以了，递归过程不用管
    if n==0:
        return
    #! 把n-1，从A移动到B
    Move(n-1, A, C, B)
    #! 只剩下最后的，直接移动
    print("{}->{}".format(A, C))
    #! 把剩下的n-1，从B移动到C
    Move(n-1, B, A, C)
    
Move(3,'A','B','C')