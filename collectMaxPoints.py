row,col=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(row)]
for i in range(1,col):
    for j in range(row):
        if j==0:
            matrix[j][i]+=max(matrix[j][i-1],matrix[j+1][i-1])
        elif j==row-1:
            matrix[j][i]+=max(matrix[j][i-1],matrix[j-1][i-1])
        else:
            matrix[j][i]+=max(matrix[j][i-1],matrix[j-1][i-1],matrix[j+1][i-1])
print(max(matrix[i][col-1] for i in range(row)))
'''
#col=1 
row=0 
prev=[2,5]
5 8 3
2 1 4
0 9 4
row =1
prevs=[5,0,2]
5 8 3
2 6 4
0 9 4
row=2 
prevs=[2,0]
5 8 3
2 6 4
0 11 4
#col=2 
row=0
prevs=[6,8]
5 8 11
2 6 4
0 11 4
row=1 
prevs=[8,11,6]
5 8 11
2 6 15
0 11 4
row=2
prevs[6,11]
5 8 11
2 6 15
0 11 15
'''

'''n=int(input())
total=0
maxtotal=0
li=list(map(int,input().split()))
for i in range(n-1):
    if li[i]<li[i+1]:
        total+=li[i]
    else:
        total+=li[i]
        if total>maxtotal:
            maxtotal=total
        total=0
total+=li[-1]
if total>maxtotal:
    maxtotal=total
print(maxtotal)'''
