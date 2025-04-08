import sys
input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    a = list(input().strip())
    a = sorted(a)
    if a[0] != a[x - 1]: # 给每一个都分配一个如果不完全相同
        # print(1)
        print(a[x - 1])
        return
    # 给每一个都分配了相同的而且都是最大的
    print(a[0], end = '')
    if a[x] != a[n - 1]: # 当前的不是最大的那一个
        # 把剩下的均匀分配
        # print(2)
        for i in range(x, n):
            print(a[i], end = '')
    else:
        # print(3)
        
        for i in range((n - 1) // x):
            print(a[n - 1], end='')
        
main()
