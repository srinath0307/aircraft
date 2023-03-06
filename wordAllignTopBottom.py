'''s=input().strip()
r=max([len(word) for word in s])
c=len(s)
matrix=[["*" for col in range(c)]for row in range(r)]

for index in range(len(s)):
    if index%2==0:
        for row in range(len(s[index])):
            matrix[row][index]=s[index][row]
    else:
        matrix[index]=s[index]
        for row in range(len(s[index])):
            matrix[r-row-1][index]=s[index][row]
for i in matrix:
    print(*i)
'''
'''
bricks stones vegetables fruits grains
'''

