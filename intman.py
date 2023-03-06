word=input().strip()
r=(len(word)+1)//2      #5
c=len(word)             #9
matrix=[['*' for col in range(c)]for row in range(r)]
row=0
col=0
for index in range((len(word)//2)+1):
    matrix[row][col]=word[index]
    matrix[r-row-1][col]=word[index]
    matrix[row][c-col-1]=word[len(word)-index-1]
    matrix[r-row-1][c - col - 1] = word[len(word) - index - 1]
    row+=1
    col+=1
'''for i in range(row):
    for j in range(col):
        print(*matrix)'''
for i in matrix:
    print(*i,sep="")



