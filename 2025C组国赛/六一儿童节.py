
cnt = 0
for x in range(1, 20240601 + 1):
    for y in range(x + 1, 20240601 + 1):
        if (x**x + y**y) % 6421 == 0:
            cnt += 1

print(cnt)
