n=int(input())
numList=[int(val) for val in input().split()];matrix=[]
j=int(input())
for i in range(j):
    x,y,direction=map(str,input().split())
    x=int(x)-1;y=int(y)
    if direction=='R':
        numList[x + 1:y], numList[x]= numList[x:y - 1], numList[y - 1]

    if direction=='L':
        numList[x:y - 1], numList[y - 1]= numList[x + 1:y], numList[x]
    matrix.append(numList[::])
    print(numList)
print(matrix)
''' 
9
25 36 6 18 15 51 95 78 90
4
1 3 L
2 8 R
6 9 R
1 9 L
'''
