'''#n=int(input())
curr='1000999998997996995994'
flg=0
for i in range(1,len(curr)//2):
    ctr=int(curr[-i:])
    currNum=str(ctr)
    ctr+=1
    while len(currNum)<len(curr):
        currNum=str(ctr)+currNum
        ctr+=1
    if currNum==curr:
        print(ctr-1)
        flg=1
        break
if flg==0:
    print("no")'''

'''
def printSeries(m,n):
    ctr=m 
    while ctr>=n:
        print(ctr,end="")
        ctr-=1
x,y,z=map(int,input().split())
if x>y:
    printSeries(x,y)
else:
    printSeries(y,z)
if x>y:
    printSeries(y,z)
else:
    printSeries(x,y)'''




'''

s=input().split()
length=len(s)
ctr=0
for i in range(length):
    for j in range(length):
        if i!=j:
            if s[i]+s[j]==(s[i]+s[j])[::-1]:
                ctr+=1
print(ctr)'''
'''s=input().split()[::-1]
ctr=1
for i in range(len(s)):
    if ctr%2==1:
        print(s[i],end=" ")
    else:
        print(s[i][::-1],end=" ")
    ctr+=1
'''

'''
n=int(input())
matrix=[]
for i in range(n):
    li=[]
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==j or j==n-i-1:
            li.append('*')
        else:
            li.append('-')
    matrix.append(li)
for i in matrix:
    print(*i,sep='')
'''
'''r,c=map(int,input().split())
matrix=[]
for i in range(r):
    li=list(map(int,input().split()))
    matrix.append(li)
total=0
for i in range(r):
    for j in range(c):
        if not i==0 or j==0 or i==r-1 or j==c-1:
            total+=matrix[i][j]
print(total)'''

'''n=int(input())
li=list(map(int,input().split()))
l=[]
for i in li:
    if i%2==0:
        l.append(i)
print(*l[::-1])
'''
'''
#left odd right odd count optimized
n=int(input())
oddCount = 0
li=list(map(int,input().split()))
for i in li:
    if i%2 == 1:
        oddCount += 1
if li[0]%2 != 0:
    oddCount -= 1
left = 0
right = oddCount
for i in range(n-1):
    if left == right:
        print(li[i], end=" ")
    else:
        print(-1,end=' ')
    if li[i+1] % 2 == 1:
        right -= 1   #1 3 4 8 5 7
    if li[i] % 2 == 1:
        left += 1
if left == right:
    print(li[-1], end=" ")
else:
    print(-1, end=' ')'''






'''n=int(input())
li=list(map(int,input().split()))
for i in range(n):
    left=0
    right=0
    for j in range(i):
        if li[j]%2!=0:
            left+=1
    for j in range(i+1,n):
        if li[j]%2!=0:
            right+=1
    if left==right:
        print(li[i],end=" ")
    else:
        print(-1,end=" ")'''
#1 3 4 8 5 7



'''s1=input()
s2=input()
stack1=[];stack2=[]
for i in s1:
    if i!='#':
        stack1.append(i)
    elif i=='#':
        if stack1!=[]:
            stack1.pop()
for i in s2:
    if i!='#':
        stack2.append(i)
    elif i=='#':
        if stack2!=[]:
            stack2.pop()
print(stack1,stack2)'''
'''
stack=[k,e]

'''



''' 
last in first out 

'''




''' 
queue first in first out
queue=[5]
queue.append(6)
queue.append(7)
queue.pop(0)
print(queue)
'''
#longest common subsequence
s1=input().strip()
s2=input().strip()
n=len(s1)
m=len(s2)
dp=[[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if s1[i-1]==s2[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[n][m])

#joshephus problem
n=int(input())
k=int(input())
li=[i for i in range(1,n+1)]
i=0
while len(li)>1:
    i=(i+k-1)%len(li)
    li.pop(i)
print(li[0])
# number of possible ways for reaching all cities from 1st city
n=int(input())
li=list(map(int,input().split()))
dp=[0 for i in range(n)]
dp[0]=1
for i in range(1,n):
    for j in range(i):
        if li[j]+j>=i:
            dp[i]+=dp[j]
print(dp[-1])
# dividing apples in k baskets
n=int(input())
k=int(input())
dp=[[0 for i in range(k+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        if i<j:
            dp[i][j]=0
        elif i==j:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
print(dp[n][k])
#pendulum problem
n=int(input())
li=list(map(int,input().split()))
li.sort()
ans=[]
for i in range(n):
    if i%2==0:
        ans.append(li[i//2])
    else:
        ans.append(li[n-i//2-1])
print(*ans)
#karatsuba multiplication
def karatsuba(x,y):
    if x<10 or y<10:
        return x*y
    n=max(len(str(x)),len(str(y)))
    nby2=n//2
    a=x//(10**nby2)
    b=x%(10**nby2)
    c=y//(10**nby2)
    d=y%(10**nby2)
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    adbc=karatsuba(a+b,c+d)-ac-bd
    prod=ac*(10**(2*nby2))+adbc*(10**nby2)+bd
    return prod
#booths algorithm
def booth(multiplicand,multiplier):
    multiplicand=bin(multiplicand)[2:]
    multiplier=bin(multiplier)[2:]
    n=len(multiplier)
    multiplicand=multiplicand.zfill(n)
    multiplier=multiplier.zfill(n)
    A=multiplicand
    Q=multiplier
    M='0'*n
    Q0='0'
    for i in range(n):
        if Q0=='0' and Q[-1]=='1':
            A=add(A,M)
        elif Q0=='1' and Q[-1]=='0':
            A=add(A,complement(M))
        Q0=Q[-1]
        Q=shift(Q)
        Q=Q[0]+A[-1]
        A=shift(A)
    return A,Q
def complement(A):
    A=''.join(['1' if i=='0' else '0' for i in A])
    return A
def add(A,B):
    n=len(A)
    A=int(A,2)
    B=int(B,2)
    C=A+B
    C=bin(C)[2:]
    C=C.zfill(n)
    return C
def shift(A):
    A='0'+A[:-1]
    return A
#binary palindromes
n=int(input())
li=list(map(int,input().split()))
for i in range(n):
    if li[i]==1:
        print(1)
    else:
        print(2**(li[i]-1),end=" ")



