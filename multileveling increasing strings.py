'''levels=[]
levels.append([1 for i in range(51)])
for i in range(1,10):
    level=[]
    for j in range(i):
        level.append(0)
    level.append(1)'''
'''level=[0,1]
i=1
j=i
for k in range(51):
    summm=0
    for l in level[j-i:i+j]:
        summm+=l
        print(level)
        print(l)
        j+=1
    level.append(summm)
print(level)
'''
N,T=map(int,input().split())
series=[0]*(N-1)
series.extend([1,1])
print(series)
for ctr in range(T):
    series.append(sum(series[len(series)-N:]))
print(*series)

