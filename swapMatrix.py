r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()]for row in range(r)]
x,y,k=map(int,input().split())
x-=1
y-=1
for row in range(k//2):
    matrix[x+row][y:y+k],matrix[x+k-row-1][y:y+k]=matrix[x+k-row-1][y:y+k],matrix[x+row][y:y+k]
for i in matrix:
    print(*i)
'''
5 8
55 56 19 46 44 69 15 40
92 64 35 95 59 98 53 54
82 78 81 86 61 38 27 39
75 17 20 84 72 12 29 79
26 34 30 62 68 51 21 91
2 2 3
'''