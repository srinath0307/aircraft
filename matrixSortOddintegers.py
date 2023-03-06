'''r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()] for row in range(r)]
oddint=[]
for row in range(r):
    for col in range(c):
        if matrix[row][col]%2!=0:
            oddint.append(matrix[row][col])
oddintk=sorted(oddint)
ctr=0
for row in range(r):
    for col in range(c):
        if matrix[row][col] % 2 != 0:
            matrix[row][col]=oddintk[ctr]
            ctr+=1
for i in matrix:
    print(*i)'''


'''
3 4
90 5 85 29
53 9 17 88
16 99 41 21
'''
''' 
5 7
644 74 347 76 782 172 783
739 281 601 600 30 431 608
437 778 199 396 253 352 687
799 648 101 583 542 42 997
58 667 581 597 499 579 933
'''
n=input().strip()
first=n[:2];last=n[-2:]
print(abs(int(first)-int(last)))
