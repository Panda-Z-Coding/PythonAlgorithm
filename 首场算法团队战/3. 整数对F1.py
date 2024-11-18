'''
def get_presum(arr):#下标从0开始
    n = len(arr)
    sum = [0] * n
    sum[0] = arr[0]
    for i in range(1,n):
        sum[i] = sum[i-1] + arr[i]
    return sum

# 求区间[l,r]的和
# a[l]+...+a[r] = sum[r] - sum[l-1]

def get_sum(sum,l,r):
    if l == 0:
        return sum[r]
    else:
        return sum[r] - sum[l - 1]

N = int(input())

A = list(map(int, input().split()))
pre = get_presum(A)
ans = 0
for i in range(N):
    for j in range(N):
        ans += get_sum(pre, i, j)
print(ans)
'''
#前缀和不行，也是O(n^2)
    

N = int(input())

A = list(map(int, input().split()))
ans = 0

for k in range(N):
    ans += A[k]*(k+1)*(N-k) # 计算对答案的贡献值

print(ans)

