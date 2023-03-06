p=int(input("enter the row number:"))
q=int(input("enter the column number:"))
n=int(input("enter the column number matrix1  or row number of matrix 2:"))
print("enter the numbers of first matrix")
matrix1=[[int(input())for i in range(n)]for j in range(p)]
print("enter the second matris elements")
matrix2=[[int(input()) for i in range(n)]for j in range(q)]
result=[[0 for i in range(q)]for j in range(p)]
for i in range(p):
      for j in range(q):
            for k in range(n):
                result[i][j]=result[i][j]+matrix1[i][k]+matrix2[j][k]
print("result is:")
for i in range(p):
      for j in range(q):
            print(result[i][j],end="\t")
      print("\n")
