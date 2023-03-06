import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

matrix = []
print("Enter the entries rowwise:")
  
#User input
for i in range(R):
    a =[]
    for j in range(C):      
         a.append(int(input()))
    matrix.append(a)
#matrix=[[int(input()) for j in range(C)]for i in range(R)]
#Printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
#Decomposition of the matrix
q, r = np.linalg.qr(matrix)
print('\nQ:\n', q)
print('\nR:\n', r)
