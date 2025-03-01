import bisect

#! 我们定义一个tails数组：tails[i] => 所有长度为i + 1的递增子序列中，结尾元素的最小值
#? 这是一种贪心的算法，我们让结尾的数字越小，那我们在后面就能添加更多的上升元素
#? 我们要维护每一个长度lis的结尾最小值
#? 用二分查找减少对数组便利，提高查找效率

def len_Of_LIS(arr):
    # 两种操作
    #? 1. 当要插入tails数组的位置是数组的长度的时候，将这个点数append
    #? 2. 当要插入tails数组的位置在数组内时，把这个位置更新成这个数
    #! 最后tails的长度就是LIS的长度
    tails = []
    for num in arr: # 便利初始数组
        pos = bisect.bisect_left(tails, num) # 在tails中查找插入num的位置
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)

arr = [3, 5, 2, 8, 4, 6]
print(len_Of_LIS(arr))