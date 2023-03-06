'''r,c=map(int,input().split())
matrix=[list(map(int,input().split())) for _ in range(r)]
j=1
while j<c:
    lsum=0;rsum=0
    for col in range(j):
        for row in range(r):
            lsum+=matrix[row][col]
    for k in range(j,c):
        for l in range(r):
            rsum+=matrix[l][k]
    if lsum==rsum:
        print("YES")
        exit()
    j+=1
print("NO")'''



'''   2<4
ind=0 1 2 3
    1 2 3 4   (0,3)
    1 2 3 4
    1 2 3 4
    1 2 3 4 
'''
''' 
4 4
10 4 4 5
10 5 3 4
20 3 5 3
10 6 2 6
'''








