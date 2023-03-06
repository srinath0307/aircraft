'''r,c=map(int,input().split())
matrix=[[val for val in input().split()] for row in range(r)]
for row in range(r):
    for col in range(c):
        if matrix[row][col]=='+':
            matrix[row][col]=int(matrix[row-1][col])+int(matrix[row+1][col])
        elif matrix[row][col]=='-':
            matrix[row][col]=abs(int(matrix[row-1][col])-int(matrix[row+1][col]))
for i in matrix:
    print(*i)'''
''' 
4 3
10 30 60
+ - 70
20 95 +
25 50 10
'''
'''li=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=int(input())
for i in range(n):
    a=input().strip()
    di={}
    for j in a:
        if j not in di:
            di[j]=1
        else:
            di[j]+=1
    flag=True
    for i in di:
        c=li.index(i)
        if di[i]==c+1:
            flag=True
        else:
            flag=False
    if flag:
        print("Yes")
    else:
        print("No")'''





'''n=int(input())
li=['0','1']
for i in range(n-2):
    li.append(li[-2]+li[-1])
for j in li:
    print(j)
for k in li[:len(li)-1][::-1]:
    print(k)'''

n=int(input())
l=[bin(i)[2:] for i in range(n,0,-1)]
i=0
while i<len(l[0]):
    for j in l:
        if i<len(j):
            print(j[i],end="")
    i+=1
    print()













