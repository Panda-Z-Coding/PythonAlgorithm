import bisect

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [A[i] - B[i] for i in range(n)]
sorted_C = sorted(C)

sum_total = 0
for x in C:
    target = -x
    pos = bisect.bisect_right(sorted_C, target)
    sum_total += n - pos

count = sum(1 for x in C if x > 0)
print(sum_total - count)
