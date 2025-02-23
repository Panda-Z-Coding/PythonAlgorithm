import os
import sys

# 请在此输入您的代码
def minimize_height_diff(heights, n, k):
    heights.sort()

    if k == n:
        return 0
    if k == 1:
        return heights[-1] - heights[0]

    left, right = 0, heights[-1] - heights[0]

    while left < right: #当左右相等时候结束
        mid = (left + right) // 2
        count = 1
        current_min = heights[0]

        '''
        下面这一步：
            我们给定的mid是这次while的最大极差
            我们便利数组,让当前便利的数差值不大于mid成为一组,如果差值大于mid就新开一个组给他,让他成为当前组的最小值
            便利数组后,我们得到了如果要满足极差mid来分组的分组数量,如果不满足k
            分组数量大于k,说明 : 分太多了,极差太小了
            分组数量小于k,说明 : 分太少了,极差太大,我们贪心,让mid变小
        '''
        for i in range(1,n):
            if heights[i] - current_min > mid:
                #加一组
                count += 1
                current_min = heights[i]
                if count > k:
                    break
            #else 如果差值不大于mid的话就默认加入数组，我们知道等到有一个差值大于mid数然后加一组，更新当前组的最小值就可以了
        
        if count <= k:
            #贪心，count 满足了小于k，那我们贪心想让mid更小，所以我们就让right(可能最大的最大的极差变小)
            right = mid
        else:
            #如果不满足的话，我们的mid取太小了，就让left(最小可能的最大值)+1
            left = mid + 1
    return left



n, k =map(int, input().split())
# nums = [int(x) for x in input().split()]
nums = list(map(int, input().split()))

print(minimize_height_diff(nums, n, k))



