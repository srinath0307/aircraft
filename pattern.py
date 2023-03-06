'''n=int(input())
li=[]
while n!=1:
    a=[]
    for i in range(n):
        a.append(n-i)
    li.append(a)
    n-=1
for i in range(len(li)):
    print(*li[i],sep="")
print(1)
li=li[::-1]
for i in range(len(li)):
    print(*li[i][::-1],sep="")'''
'''n=int(input())
ctr=1
o=n
matrix=[[n for i in range((n*2)-1)] for _ in range((n*2)-1)]
n-=1
row=n*2
col=1
l=[0,1,2,3,4,5,6]
print(l)
while n>0:
    #print(n)
    for i in range(ctr,row):
        for j in range(col,(o*2)-col-1):
            matrix[i][j]=n
    row-=1
    col+=1
    ctr+=1
    n-=1
for i in matrix:
    print(*i,sep='')'''
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
N=int(input())
R=C=N*2-1
matrix=[[1 for col in range(C)] for row in range(R)]
num=N
for ctr in range(R//2):
    for row in range(ctr,R-ctr):
        for col in range(ctr,C-ctr):
            matrix[row][col]=num
    num-=1
if R%2:
    matrix[R//2][C//2]=num
for row in matrix:
    print(*row,sep="")









