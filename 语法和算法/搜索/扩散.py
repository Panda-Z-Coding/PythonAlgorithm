ans = 0
for i in range(-2020, 4041):
    for j in range(-2020, 4021):
        if any(abs(i - x) + abs(j - y) <= 2020 for x, y in [(0, 0), (2020, 11), (11, 14), (2000, 2000)]):
            ans += 1
print(ans)

#? any函数 => 如果容器中存在元素 -> True