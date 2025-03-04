 #? 23Py-A
 
def leap(y):
    # 用来判断是否是闰年
    return y % 400 == 0 or y % 4 == 0 and y % 100 != 0
ans = 0
d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 每个月的天数,注意下标
for y in range(2000, 1999999 + 1): # 年
    # 按照年份更改二月的天数
    if leap(y): d[1] = 29
    else: d[1] = 28
    for m in range(1, 12 + 1):
        for day in range(1, d[m - 1] + 1):
            if (y % m) == 0 and (y % day) == 0:
                ans += 1
ans += 1
print(ans) # 35813063