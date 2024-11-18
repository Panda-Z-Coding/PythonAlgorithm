
t = int(input())
for _ in range(t):
    s = input()
    if s[0] == '0':
        print(int(s) + 1)
    else:
        print(s + '0')
