from bisect import *
def Discrete1(a): #二分查找
    """
    :param a:   输入列表a
    :return:    返回离散化的列表
    """
    
    #1 拷贝一份 b,排序&去重
    b = list(set(a)) # 集合去重
    b.sort()
    print(b)
    #2 对每个元素找到离散化位置
    ans = []
    # 对a中的每个元素,将x转化为b列表的下标
    for x in a:
        ans.append(bisect_left(b, x) + 1) # 从1开始 -> from bisect import *
    return ans

def Discrete2(a): # 字典查找
    """
    :param a:   输入列表a
    :return:    返回离散化的列表
    """
    
    #1 拷贝一份 b,排序&去重
    b = list(set(a)) # 集合去重
    b.sort()
    print(b)
    
    dic = dict(zip(b, list(range(1,len(b)+1)))) #从1开始
    # zip(b, list(range(1,len(b)+1))) -> 把b的每一个元素对应的下标组装起来
    #2 对每个元素找到离散化位置
    ans = []
    # 对a中的每个元素,将x转化为b列表的下标
    for x in a:
        ans.append(dic[x]) # 从1开始
    return ans

a = list(map(str, input().split()))

print(Discrete1(a))
print(Discrete2(a))

'''
运用 -> 树状数组、线段树等结构
当做下标使用
'''