ans = 0

def find_i(s):
    find_1 = s.find('2')
    if find_1 == -1:
        return 0
    find_2 = s.find('0', find_1 + 1)
    if find_2 == - 1:
        return 0
    find_3 = s.find('2', find_2 + 1)
    if find_3 == -1:
        return 0
    find_4 = s.find('3', find_3 + 1)
    if find_4 == -1:
        return 0

    return 1
    
for i in range(12345678, 98765432 + 1):
    s = str(i)
    if find_i(s) == 0:
        ans += 1    


print(ans)
