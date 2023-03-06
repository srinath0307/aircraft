'''matrix=[
    [1,2,3,90,9],
    [4,5,6,13,99],
]
r=2
c=5
submain=[]
for i in range(r-1):
    for j in range(c-1):
        submatrx=[]
        submatrx.append(matrix[i][j])
        submatrx.append(matrix[i][j+1])
        submatrx.append(matrix[i+1][j])
        submatrx.append(matrix[i+1][j+1])
        submain.append(submatrx)
print(submain)'''
'''n,k=map(int,input().split())
li=[int(val) for val in input().split()]
for i in range(0,n-1,k):
    unit=''
    for j in range(i,i+k):
        unit+=str(li[j]%10)
        print(j)
    if int(unit)==0:
        print(0,end=" ")
    else:
        for j in range(1,int(unit)+1):
            if int(unit)%k==0:
                print(k,end=" ")
    print()'''
'''
12 4
20 81 20 86 61 20 22 54 10 120 21 73
'''
'''li=[]
n,x=map(int,input().split())
for i in range(n):
    num,pos=map(int,input().split())
    li.append([num,pos])
li=sorted(li,key=lambda x:x[1])
print(min(li[-1][0],li[-2][0]),max(li[-1][0],li[-2][0]))'''
''' 
5 2
3 7
1 9
2 0
5 15
4 30
'''
'''n=int(input())
li=list(map(int,input().split()))  # 3 2 0 1
k=[int(val) for val in range(n)] #0 1 2 3
s=[]                            #2 3 1 0
for i in li:
    for j in k:
        if i==j:
            s.append(k.index(j))
print(*s)'''
'''def reaarrangenaive(arr,n):
    temp=[0]*n
    for i in range(0,n):
        temp[arr[i]]=i
    for i in range(0,n):
        arr[i]=temp[i]
    return arr
n=int(input())
arr=list(map(int,input().split()))
print(*reaarrangenaive(arr,n))'''

'''n=int(input())
s=input().strip()
print(s.count(str(n)))'''


n=int(input())
li=list(map(int,input().split()))
k,x=map(int,input().split())
l=[]
for i in li:
    if len(str(abs(i)))==k:
        l.append(i)
l.sort()
print(l)
try:
    print(l[x-1])
except:
    print(-1)
''' 
6
-95 -5254 -13 -20 -654 -40
2 3
'''







