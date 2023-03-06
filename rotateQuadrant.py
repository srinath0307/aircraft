r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()]for row in range(r)]
k=int(input())
for ctr in range(k):
    for row in range(r//2):
        matrix[row][:c//2],matrix[row][c//2:],matrix[r//2+row][c//2:],matrix[r//2+row][c//2:],matrix[r//2+row][:c//2]=matrix[r//2+row][:c//2],matrix[row][:c//2],matrix[row][c//2:],matrix[row][c//2:],matrix[r//2+row][c//2:]
for i in matrix:
    print(*i)

''' 
4 4
10 20 11 22                              55 66 10 20 
30 40 33 44                              77 88 30 40 
55 66 50 60                              11 22 55 66
77 88 70 80                              30 4
2 
'''
''' 
4 6
14 11 20 72 41 96
42 48 80 75 87 39
28 54 73 61 25 44
89 81 31 29 47 78
7
'''