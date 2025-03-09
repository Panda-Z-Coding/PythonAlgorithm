from itertools import combinations, permutations

s = 'abcdefg'

ans, cnt = [], 0

for i in range(1, 8):
    for x in combinations(s, i):
        ans.append("".join(x))

# 要求相连
dict = {
    'a':['f', 'b'],
    'b':['a', 'c', 'g'],
    'c':['b', 'g'],
    'd':['e', 'c'],
    'e':['g','d','f'],
    'f':['a', 'g', 'e'],
    'g':['f','b','e','c']
}

for str1 in ans:
    if len(str1) == 1:
        cnt+= 1
        continue

    for s1 in permutations(str1):
        flag = 1
        for i in range(1, len(s1)):
            if s1[i-1] not in dict[s1[i]]:
                flag = 0
                break   
        if flag:
            cnt += 1
            break
print(cnt)
