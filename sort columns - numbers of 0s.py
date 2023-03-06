r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()] for row in range(r)]
trmat=[sorted(list(row))for row in zip(*matrix)]
trmat=sorted(trmat,key=lambda x:x.count(0))
for row in zip(*trmat):
    print(*row)
"""
6 5
0 1 1 0 0
0 1 0 0 1
0 1 1 0 0
1 1 0 0 1
1 0 1 0 0
0 0 0 0 0
"""
