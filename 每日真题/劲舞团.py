max_k = 0
k=0
time=0
for _ in range(2000):
    data = input().split()
    if data[0]==data[1] and int(data[2])-time<=1000:
        k+=1
        max_k=max(k,max_k)
    else:
        k=0
    time=int(data[2]) # 存储上一个的时间戳
print(max_k+1)
