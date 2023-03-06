'''def isValid(S1,S2):
    for ch in S2:
        if ch not in S1:
            return False
        S1=S1.replace(ch,"",1)
    return True
S1,S2=input().split()
for L in range(len(S2),len(S1)+1):
    for index in range(len(S1)-L+1):
        if isValid(S1[index:index+L],S2):
            print(S1[index:index+L])
            exit()
print(-1)'''
'''
environment nee 

hello world cd
'''

'''#Your code below
n=int(input())
matrix=[input().split() for _ in range(n)]
revLi=[];ctr=0
for i in range(n-1,-1,-1):
    if ctr%2==0:
        for j in range(n-1,-1,-1):
            revLi.append(matrix[i][j])
    else:
        for j in range(n):
            revLi.append(matrix[i][j])
    ctr+=1
forward=[]
for i in range(n):
        if i % 2 == 0:
            for j in range(n):
                forward.append(matrix[i][j])
        else:
            for j in range(n-1,-1,-1):
                forward.append(matrix[i][j])
print(forward)
print(revLi)
ctr=0
if n%2==0:
    ctr=0
else:
    ctr=1
for i in range((len(forward)//2)+ctr):
    if forward[i]==revLi[i]:
        print(forward[i],end=' ')
        flag=1
if flag==0:
    print("1-")'''
'''
N=int(input())
mat=[list(map(str,input().split())) for i in range(N)]
ctr=0
for i in range((N+1)//2):
    if(i%2==0):
        for j in range(N):
            if(mat[i][j]==mat[-1*(i+1)][::-1][j]):
                print(mat[i][j],end=" ")
                ctr=1
    else:
        for j in range(N):
            if(mat[i][::-1][j]==mat[-1*(i+1)][j]):
                print(mat[i][::-1][j],end=" ")
                ctr=1
if not ctr:
    print("-1")
'''
''' 
6
m o h n g i
t s v u h r
g l m n n o
o c b d f g
r h v v s t
o g i g f e
'''


'''
s='en1VebfTXArQA30EpZNVQrMWM57McEdI4nCwWu6SA6vsZtoRF3fTaN3X69qQMDwYtYNKnTG2wDrnbV0fHAkd8Bs4g6IXCfpvrn8F'
tot=0
for i in s:
    if i.isnumeric():
        tot+=int(i)
print(tot)
for i in s:
    if i.isalpha():
        i=i.lower()
        print(chr(ord(i)+tot),ord(i)+tot,ord(i))'''



n=12
binVal=bin(n)[2:]
l=[]
'''for i in range(len(binVal)):
    iterVal=''
    for j in range(i,len(binVal)):
        iterVal+=binVal[j]
        val=int(iterVal,2)
        if val not in l:
            l.append(val)
print(*l)'''
'''for i in range(len(binVal)):
    for j in range(i,len(binVal)):
        iterVal=int(binVal[i:j+1],2)
        if iterVal not in l:
            l.append(iterVal)
print(*l)'''
words=["abc",'deq','mee','aqq','dkd','ccc']
pattern='abb'
'''def findAndReplacePattern(words, pattern):
    def match(word):
        m1, m2 = {}, {}
        for w, p in zip(word, pattern):
            if w not in m1: m1[w] = p
            if p not in m2: m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True

    return filter(match, words)'''





'''s=input().strip()
row,col=map(int,input().split())
words=[]
for i in range(row):
    words.append(input().split())
total=0
for i in range(row):
    for j in range(col):
        for k in range(j,col):
            sub=''
            for l in words[i][j:k]:
                sub+=l
            if sub==s:
                total+=1
print(total)'''

'''

n=int(input())
start,add,middle=1,n//2+1,(n//2)*2-1
for ctr in range(n//2):
    right=list(map(str,range(start,start+add)))
    left='-'.join(right[::-1])
    right='-'.join(right)
    if ctr%2:
        left,right=right,left
    print('-'*ctr*3,right,"-"*middle,left,sep='')
    start+=add
    add-=1
    middle-=2
print('-'*3*(n//2)+"0")
start,add,padd=1,2,n//2-1
for ctr in range(1,n//2+1):
    right=list(map(str,range(start,start+add)))
    left='-'.join(right[::-1])
    right='-'.join(right)
    if(ctr%2):
        left,right=right,left
    print("-"*3*padd,right,"-"*(2*ctr-1),left,sep="")
    start+=add
    add+=1
    padd-=1'''


'''n=int(input())
li=[]
corners=0
center=(n+n)-3
for i in range(n-1):
    s=''
    s+='*'*corners
    s+=str(i+1)
    s+='*'*center
    s+=str(i+1)
    s+='*'*corners
    li.append(s)
    corners+=1
    center-=2
for i in li:
    print(i)
print('*'*corners+str(n)+'*'*corners)
for i in li[::-1]:
    print(i)'''