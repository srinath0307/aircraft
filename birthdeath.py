'''row=int(input())
col=int(input())
matrix=[[int(input()) for x in range(col)]for y in range(row)]
for i in range(row):
	a=[]
	for j in range(col):
		a.append(int(input()))
	matrix.append(a)
print(matrix)
corners=[]
corners.append(matrix[0][0])
corners.append(matrix[0][row-1])
corners.append(matrix[col-1][0])
corners.append(matrix[row-1][col-1])
corner_sum=0
for i in corners:
	corner_sum+=i
print(corner_sum)
for i in range(row):
	for j in range(col):
		print(matrix[i][j],end=" ")
	print()
'''
'''n=int(input())
lifespan=[]
for i in range(n):
    birth,death=map(int,input().split())
    lifespan.append([birth,death])
y=int(input())
count=0
for fromy,toy in lifespan:
    if fromy<=y and toy>y:
        count+=1
print(count)'''
"""
8
2000 2021
1947 1989
1940 2011
2001 2019
1945 2000
1975 2005
2002 2020
1960 1999
2000
"""

'''
from collections import Counter
li=list(map(int,input().split()))
li2=[]
li3=[]
for i in li:
    for j in str(i):
        li2.append(j)
counter1=Counter(li2)
for i in counter1:
    if counter1[i]<=min(counter1.values()):
        li3.append(i)
li3.sort()
print(li3)'''


'''s='karfdiukjwbdfikbldkfbcldkfcbvc'
d={} #{'k':2,'a':1,'r':1}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
li=[]
for i in d:
    li.append([i,d[i]])
print(li)
li=sorted(li,key=lambda x:(x[1],x[0]))
print(li)
minVal=li[0][1]
for i in li:
    if i[1]==minVal:
        print(i[0],end=' ')
    else:
        break

'''












