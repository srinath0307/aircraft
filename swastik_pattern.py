n = int(input())
matrix = []
s = list('*' * n)
for i in range(n):
    matrix.append(s.copy())
ctr = 1
for i in range((n // 2) + 1):  # i= 0, 1, 2
    matrix[i][0] = ctr  #
    matrix[n - 1][i] = ctr
    matrix[0][n - i - 1] = ctr
    matrix[n - i - 1][n - 1] = ctr
    ctr += 1
for i in range(1, n - 1):
    matrix[n // 2][i] = ctr
    matrix[i][n // 2] = ctr
    ctr += 1
for i in range(n):
    print(*matrix[i])
