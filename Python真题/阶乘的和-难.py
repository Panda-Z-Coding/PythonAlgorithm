n = int(input())
a = list(map(int, input().split()))
b = [0] * (100000 + 1)
ok = True
Min = 100000
for i in range(1, n + 1):
    if a[i - 1] >= 100000:
        Min = min(a[i - 1], Min)
    else:
        b[a[i - 1]] += 1
        ok = False
if ok:
    print(Min)
else:
    for i in range(1, 100001):
        if ((b[i] % (i + 1)) != 0):
            print(i)
            break
        else:
            b[i + 1] += (b[i] // (i + 1))
            # 2 2 2 -> 合成一个 3
            # 所以原来的个数因为是可以合成的
            # 所以直接整除算出最大能合成的数
