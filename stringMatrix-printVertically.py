'''s1=input().strip()
s2=input().strip()
s3=input().strip()
matrix=[["*" for c in range(len(s1))] for r in range(max(len(s2),len(s3)))]
col=0
while col<len(s1):
    for k in s1:
        matrix[0][col]=s1[col]
    col+=1
s3flag=False;s2flag=False
for col in range(len(s1)):
    if s1[col]==s2[0] and s2flag==False:
        for row in range(len(s2)):
            matrix[row][col]=s2[row]
        s2flag=True
    elif s1[col]==s3[0] and s3flag==False:
        for row in range(len(s3)):
            matrix[row][col]=s3[row]
        s3flag=True
for i in matrix:
    print(*i,sep="")'''

""" 
butter
toy
task
"""

s1=input().strip()         #butter
s2=input().strip()         #toy
s3=input().strip()         #task
matrix=[["*" for c in range(len(s1))] for r in range(max(len(s2),len(s3)))]
col=0
while col<len(s1):
    for k in s1:
        matrix[0][col]=s1[col]
    col+=1
print(matrix)
s3flag=False;s2flag=False
for col in range(len(s1)):              #0,1,2,3,4,5
    if s1[col]==s2[0] and s2flag==False:
        for row in range(len(s2)):   #3
            matrix[row][col]=s2[row]
        s2flag=True
    elif s1[col]==s3[0] and s3flag==False:
        for row in range(len(s3)):   #3
            matrix[row][col]=s3[row]
        s3flag=True
for i in matrix:
    print(*i,sep="")















