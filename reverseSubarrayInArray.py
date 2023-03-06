L = input().split()
P = []
i = 0
Flag = 0
while(i<len(L)):
    if '[' in L[i] and ']' in L[i]:
        P.append(int(L[i][1:-1]))
    elif ']' in L[i]:
        Flag = 0
        Total.append(int(L[i][:-1]))
        Total = Total[::-1]
        P.extend(Total)
    elif '[' in L[i]:
        Total = [ int(L[i][1:]) ]
        Flag = 1
    elif Flag == 1:
        Total.append(int(L[i]))
    else:
        P.append(int(L[i]))
    i+=1
print(*P)
print(sum(P))
# 10 [20 30 40] 67 32 1 2 [90 21]
