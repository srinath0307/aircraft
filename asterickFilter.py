row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append(list(map(int, input().split())))
odd = 0
even = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] % 2 == 0:
            even += 1
        else:
            odd += 1
if even >= odd:
    for i in range(row):
        for j in range(col):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = '*'
else:
    for i in range(row):
        for j in range(col):
            if matrix[i][j] % 2 != 0:
                matrix[i][j] = '*'
nonrows = []
for i in range(row):
    ctr = 0
    for j in range(col):
        if matrix[i][j] == '*':
            ctr += 1
    if ctr == row:
        nonrows.append(i)
noncols = []
for i in range(col):
    ctr = 0
    for j in range(row):
        if matrix[j][i] == '*':
            ctr += 1
    if ctr == col:
        print(i)
        noncols.append(i)
for i in range(row):
    for j in range(col):
        if i not in nonrows and j not in noncols:
            print(matrix[i][j], end=' ')
    if i not in nonrows:
        print()
'''
5 5
1 3 5 7 9
2 4 6 8 10
1 3 5 7 9
1 3 5 7 9
1 3 5 7 9
'''
