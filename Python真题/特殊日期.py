from datetime import *
s = datetime(1900, 1, 1)
e = datetime(9999, 12, 31)
t = timedelta(days = 1)
ssum = 0
while s < e:
    y = int(s.year)
    m = int(s.month)
    d = int(s.day)
    n = y // 1000 + ((y // 10) % 10) + ((y // 100) % 10) + y % 10
    m = m % 10 + m // 10 + d % 10 + d // 10
    if n == m:
        ssum += 1
    s += t
print(ssum)
