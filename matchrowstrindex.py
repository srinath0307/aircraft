'''
r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()]for row in range(r)]
s=input().strip()
for ind1 in range(r):              #5
    for ind2 in range(ind1+1,r):    #1,6
        if (s[ind1]==s[ind2] and matrix[ind1]!=matrix[ind2]) or (s[ind1]!=s[ind2] and matrix[ind1]==matrix[ind2]):
            print("NO")
            exit()
print("YES")'''
r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()]for row in range(r)]
s=input().strip()
li=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            li.append([i,j])
for i,j in li:
    if matrix[i]!=matrix[j]:
        print("NO")
        exit()
print("YES")


''' 
5 4
2 8 8 3
6 8 7 2
2 8 8 3
9 6 3 4
6 8 7 2
ABACB
'''
''' 
6 5
10 20 30 40 50
10 20 30 40 50
60 70 80 90 99
10 20 30 40 50
60 70 80 80 99
10 20 30 40 50
GGHGHK
'''

