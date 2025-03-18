# 单调栈

# 在插入新元素的时候, 将不满足单调性质的元素弹出
#? 用途? => 求右侧第一个大于自己的元素 
# 谁把自己挤出去谁就是自己右侧第一个大于自己的元素


import os
import sys

# 单调栈

# 求右侧第一个大于自己的就从左往右入栈
# 求左侧第一个大于自己的就从右往左入栈

# 求数组a每个元素的右侧第一个大于自己的下标
def right_bigger(a, n):
    ans = [-1] * n
    # 维护递减性质
    stack = [] # 放入数字的下标
    for i, x in enumerate(a):
        # 组合起来一起遍历
        # 当栈顶元素小于x, 此时要弹出
        while len(stack) != 0 and a[stack[-1]] < x:
            # 把不满足的都给弹出来
            ans[stack[-1]] = i + 1 # x 把 stack[-1] 弹出了
            stack.pop()
        stack.append(i)
    return ans        

# 求数组a每个元素的左侧第一个大于自己的下标
def left_bigger(a, n):
    ans = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        # 反向遍历
        x = a[i]
        while len(stack) != 0 and a[stack[-1]] < x:
            ans[stack[-1]] = i + 1
            stack.pop()
        stack.append(i)
    return ans


n = int(input())
h = list(map(int, input().split()))
print(*left_bigger(h, n))
print(*right_bigger(h, n))





