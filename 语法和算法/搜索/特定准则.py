# 二分判断，check，找到最小的符合数字，往后的都是符合的



n, val = map(int, input().split())
l, r = 1, n
def check(mid):
    if mid - sum(int(x) for x in str(mid)) >= val:
        return True
    return False

while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1
    else:
        l = mid + 1

print(n - mid + 1)
