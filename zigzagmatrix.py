n=int(input())
intlist=[int(val) for val in input().split()]
r,c=map(int,input().split())
matrix=[[0]*c for row in range(r)]
row=r-1                                #2
ind=0
flag=False
while True:
    if row%2!=r%2:
        for col in range(c-1,-1,-1):
            matrix[row][col]=intlist[ind]
            ind+=1
            if ind==n:
                flag=True
                break
    else:
        for col in range(0,c):
            matrix[row][col]=intlist[ind]
            ind+=1
            if ind==n:
                flag=True
                break
    if flag==True:
        break
    row-=1
    if row==-1:
        row=r-1
for i in matrix:
    print(*i)
"""
11
10 20 30 40 11 22 33 44 50 60 70
3 3
"""