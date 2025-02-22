n, k = map(int, input().split())
yuan = list(map(int, input().split()))

# 将元宵数量较少的 n // 2 碗分给小朋友

# 进行n - k 次操作
# for i in range(1, n-k+1):
    # 从 1 -> n-k
    # 可以从区间 [i, i + k] 中把其中一碗的所有元宵倒到另一碗中
    # [1, 1 + k]...[n-k, n]
    # 类似一个长度为k 的滑动窗口,滑动n-k,遍历所有的区间

    #! 我们的任务是把比较小的 n//2 碗的和最大
    
yuan.sort()
print(sum(yuan[:n // 2]))
    
