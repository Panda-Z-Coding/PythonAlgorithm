# 单调队列处理连续k长度的最值问题 -- 滑动窗口
from collections import deque

def SlidingWindow(n, k ,nums, is_bigger):
    result = []
    queue = deque() # 存储元素的下标
    # 遍历一遍nums
    for i in range(n):
        
        if is_bigger:
            # 维护递减的单调队列, 也就是队首是最大值
            # 当末尾元素小于等于当前要进来的元素, 把末尾元素弹出
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
        else:
            # 维护递增的单调队列
            # 当末尾元素大于等于当前要进来的元素, 把末尾元素弹出
            while queue and nums[queue[-1]] >= nums[i]:
                queue.pop()
        queue.append(i)
            
        # 判断队首元素是否还在窗口里
        if queue[0] <= i - k:
            # 维持区间长度不超过长度k
            queue.popleft()
        # 队首为当前窗口的最大/最小值
        result.append(nums[queue[0]])
    return result
    
n, k = map(int, input().split())
a = list(map(int, input().split()))
G = SlidingWindow(n, k, a, True)
F = SlidingWindow(n, k, a, False)
print(max(G[i] - F[i] for i in range(n)))


