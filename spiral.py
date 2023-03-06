'''N=int(input())
matrix=[[0 for col in range(N)] for row in range(N)]
num=1
for row in range(N):
    for col in range(N):
        matrix[row][col]=num
        num+=1
for i in matrix:
    print(*i)
for ctr in range(N//2):  #ctr-(0,1)_
    for col in range(ctr,N-ctr):   #ctr=1->3
        print(matrix[ctr][col],end=" ")
    for row in range(ctr+1,N-ctr):
        print(matrix[row][N-ctr-1],end=" ")
    for col in range(N-ctr-2,ctr-1,-1):
        print(matrix[N-ctr-1][col],end=" ")
    for row in range(N-ctr-2,ctr,-1):
        print(matrix[row][ctr],end=" ")
if N%2!=0:
    print(matrix[N//2][N//2])'''
''' 
1234 
5678
9123
1234
'''
'''
input: 4 
'''
'''n=int(input())
matrix=[]
ctr=1
for i in range(n):
    sub=[]
    for j in range(ctr,ctr+n):
        sub.append(j)
    matrix.append(sub)
    ctr+=n
for i in matrix:
    print(*i)
for i in range(n//2):
    for col in range(i,n-i):
        print(matrix[i][col],end=' ')
    for row in range(i+1,n-i):
        print(matrix[row][n-i-1],end=' ')
    for col in range(n-i-2,i-1,-1):
        print(matrix[n-i-1][col],end=' ')
    for row in range(n-i-2,i,-1):
        print(matrix[row][i],end=' ')
if n%2!=0:
    print(matrix[n//2][n//2])'''

'''while True:
    try:
        p=list(map(int,input().split()))
        result.append(p)
    except:
        break'''
'''x=[[0 for i in range(len(result))] for j in range(len(result[0]))]
print(x)'''





'''
n=int(input())
matrix=[input().split() for _ in range(n)]

for ctr in range(n//2):
    for i in range(ctr,n-ctr):
        print(matrix[ctr][i],end=' ')
    for i in range(ctr+1,n-ctr):
        print(matrix[i][n-ctr-1],end=' ')
    for i in range(n-ctr-2,ctr-1,-1):
        print(matrix[n-ctr-1][i],end=' ')
    for i in range(n-ctr-2,ctr,-1):
        print(matrix[i][ctr],end=' ')
if n%2:
    print(matrix[n//2][n//2],end=' ')'''






'''
n, k = map(int, input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
li = []
while mat:
    li += mat.pop(0)
    mat = (list(zip(*mat)))[::-1]
    print(mat)
print(li[k-1])'''


'''p=input().strip()
li=list(map(str,input().strip().split()))
pli=[];o=1
for i in range(len(p)-1):
    if p[i+1]==p[i]:
        o+=1
    else:
        pli.append(o)
        o=1
if o!=0:
    pli.append(o)
ans=[]
for s in li:
    sub=[]
    o=1
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            o+=1
        else:
            sub.append(o)
            o=1
    if o!=0:
        sub.append(o)
    if sub==pli:
        ans.append(s)
if ans!=[]:
    print(-1)
else:
    print(*ans)'''


'''n=int(input())
i=0
while True:
    if str(n-i)==str(n-i)[::-1]:
        print(n-i)
        exit()
    if str(n+i)==str(n+i)[::-1]:
        print(n+i)
        exit()
    i+=1'''


'''s=input()
i=0
ctr=1
li=[]
while i<len(s)-1:
    if s[i]==s[i+1]:
        li.append(s[i])
        ctr+=1
    elif ctr>1:
        li.append(s[i])
        ctr=1
    else:
        li.append(s[i])
        li.append(s[i])
        ctr=1
if ctr==1:
    li.append(s[-1])
    li.append(s[-1])
else:
    li.append(s[-1])
print(*li,sep='')
'''










