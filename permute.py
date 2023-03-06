from itertools import permutations as permute
S=input().strip()
numList=[]
X=int(input())
for L in range(1,len(S)+1):
    for val in permute(S,L):
        print(val)
        numList.append(int("".join(val)))
numList=sorted(set(numList))
if numList[0]==0:
    numList.pop(0)
try:
    print(numList[X-1])
except:
    print(-1)