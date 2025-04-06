# 看有多少个不同的直线就可以了

points = [[x, y] for x in range(20) for y in range(21)]
docker = set() # 用于存放(k, b) 斜率截距

for i in points:
    x1, y1 = i[0], i[1]
    for j in points:
        x2, y2 = j[0], j[1]
        if x1 == x2:
            continue
        k = (y2 - y1) / (x2 - x1)
        b = (x2 * y1 - x1 * y2)/(x2 - x1)
        if (k, b) not in docker:
            docker.add((k, b))
print(len(docker) + 20)

