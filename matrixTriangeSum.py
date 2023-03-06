n=int(input())
matrix=[[int(val) for val in input().split()] for row in range(n)]
j=0;summ=0
for i in range(n):
    while j<n:
        summ+=matrix[i][j]
        j+=1
    n-=1
print(summ)
'''
4
10 20 30 40 
50 60 70 80
11 22 33 44
55 66 77 88
'''