'''n = '1000999998996'
def validator(li):
    for i in range(len(li) - 1):
        if li[i] >= li[i + 1]:
            pass
        else:
            return False
    return True
ctr = 1
li = [int(i) for i in n]
while not validator(li):
    li = []
    for i in range(0, len(n), ctr):
        li.append(int(n[i:i + ctr]))
    ctr += 1
    print(li,"wh")
print(n)
for i in range(len(li) - 1):
    if li[i] - 1 == li[i + 1]:
        pass
    else:
        print(li[i] - 1)
        break'''

'''
x,k,y,n=map(int,input().split())
if y//k>x:
    print(x*n)
else:
    print(y*(n//k)+x*(n%k))'''
'''
n = int(input())
count = [0] * 10
while n > 0:
    count[n % 10] += 1
    n //= 10
ctr = 1
while ctr <= 9:
    if count[ctr] > ctr:
        print("No")
        exit()
    ctr += 1
print("Yes")
'''
'''
n, x = map(int, input().split())
li = list(map(int, input().split()))
small = []
large = []
for i in li:
    if i < x:
        small.append(i)
    else:
        large.append(i)
c1 = len(small)
c2 = len(large)
if c1 > c2:
    print(*small)
else:
    print(*large)
'''

'''
n=int(input())
li=input().split()
numerators=[];denominators=[]
for i in li:
    x,y=map(int,i.split('/'))
    numerators.append(x)
    denominators.append(y)
print(min(numerators),max(denominators))'''

# interlace
'''r,c1,c2=map(int,input().split())
mat1=[]
for i in range(r):
    mat1.append(list(map(int,input().split())))
#print(mat1)
mat2=[]
for i in range(r):
    mat2.append(list(map(int,input().split())))
#print(mat2)
#col1=0;col2=0
for i in range(r):
    col1=0;col2=0
    while col1<c1 and col2<c2:
        print(mat1[i][col1],mat2[i][col2],end=' ')
        col1+=1
        col2+=1
    while col1<c1:  #3<5
        print(mat1[i][col1],end=' ')
        col1+=1
    while col2<c2:#3<3
        print(mat2[i][col2],end=' ')
        col2+=1
    #col1->3 col2->3
    print()
    #print(col1,col2)
'''
''' 
3 5 3
3 1 4 9 4
1 2 8 5 9
0 7 2 2 8
45 54 45
47 49 60
44 46 44
'''

'''n = int(input())
tot = 0
li = list(map(int, input().split()))
unique = set(li)
for i in unique:
    if li.count(i) > 1:
        tot += i
print(tot)
# 10 20 30 40 50 60 70
'''

'''
#<--break string values by vowels
def isvowel(ch):
    if ch in ['a', 'e', 'i', 'o', 'u']:
        return True
    return False
s = input().strip();count=0
for i in range(len(s)):
    if isvowel(s[i]):count += 1
    if count==2:
        print()
        print(s[i],end='')
        count=1
    else:
        print(s[i],end='')

n=input().strip()
f=''
for i in n:
    if i in 'aeiou' and len([i for i in f if i in 'aeiou'])!=0:
        print(f)
        f=''
    f+=i
print(f)
#helloworld
# hell
# ow
# orld
#-->
'''

'''n=input().strip()       #-9128000    int(0008219)->8219
if n[0]=='-':
    print('-')
    n=n[1:][::-1]         #  slicing ->   [start:stop:step] hello
    n=int(n)
    print(n)
else:
    n=n[::-1]
    n=int(n)
    print(n)
'''

'''
n=input().strip()
if n[0]=='-':
    print('-',end='')
    n=n[1:]
n=int(n[::-1])
print(n,end='')'''

'''

S=input().strip()
if(S[0]=='-'):
    print(-1*int(S[:0:-1]))
else:
    print(int(S[::-1]))
s="hello"
print(s[:0:-1])'''

'''
n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i,end=' ')
print()
for i in range(1,n):
    if i%2!=0:
        print(i)
'''

'''n=int(input())
ctr=1
li=[]
lines=1
for i in range(1,n+1):
    s=''
    for j in range(1,lines+1):
        if j%2==0:
            s+='*'
        else:
            s+=str(ctr)
            ctr+=1
    li.append(s)
    lines+=2
for i in li:
    print(i)
for i in li[::-1]:
    print(i)'''

'''
s=input().split()
print(s[0],end=' ')
for i in range(1,len(s)-1):
    print(s[i][::-1],end=' ')
print(s[-1],end=' ')'''

'''
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    li=[]
    for j in range(b):
        val,d=input().split()
        val=int(val)
        li.append([val,d])
    count=0;length=0;mod=0
    for k in range(len(li)):
        if k==0:
            count=li[k][0]
            mod=li[k][0]
        elif li[k][1]!=li[k-1][1]:
            li[k][0]=li[k][0]-mod
            count+=(li[k][0]//a)
        else:
            count+=((mod+li[k][0])//a)
            mod=(mod+li[k][0])%a
    print(count)
'''
'''
a,b=input().split()
s1=int(a+b)
s2=int(b+a)
k=max(s1,s2)
for i in range(1,k):
    if s1%(i**2)==0 or s2%(i**2)==0:
        print("Yes")
        exit()
print("nO")'''
'''for i in range(1,max(s1,s2)):
    if i**2==s1 or i**2==s2:
        print("Yes")
        exit()
print("No")
'''
'''li=[]
k=max(s1,s2)
for i in range(1,k):
    li.append(i**2)
for i in li:
    if i==s1 or i==s2:
        print('Yes')
        exit()
print('No')'''

'''from math import sqrt
a,b=input().split()
s1=int(a+b)
s2=int(b+a)
ans1=int(sqrt(s1))*int(sqrt(s1))
ans2=int(sqrt(s2))*int(sqrt(s2))
if ans1==s1 or ans2==s2:
    print("yes")
else:
    print("no")'''

'''s,n=input().split()
n=int(n)
li=[]
for i in s:
    if i in 'aeiouAEIOU':
        li.append(i)
if len(li)<n:
    print("-1")
else:
    print(li[:n])'''

'''
s=input().strip()
for i in range(len(s)//2):
    print(s[i])
for i in range(len(s)//2,len(s)):
    print(s[i],end=' ')'''

'''s = input().strip()
print(s)
start = 1
end = len(s) - 1
asktrisk = 1
while start < end:
    print('*' * asktrisk, end='')
    if start % 2 == 0:
        print(s[start:end], end='')
    else:
        print(s[start:end][::-1], end='')
    start += 1
    end -= 1
    asktrisk += 1
    print()'''

'''
s=input().strip()
s1=s[:len(s)//2]
s2=s[len(s)//2:]
for i in range(len(s1)):
    print(s2[i]+s1[i],end='')'''





'''a,b=input().split()
li2=[]
for i in b:
    li2.append(int(i))
li1=[]
for i in a:
    li1.append(int(i))
num=max(li2)
for i in range(len(li1)):
    if li1[i]<num:
        li1[i]=num
        break
for i in li1:
    print(i,end='')'''



'''
n=int(input())
li=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(li)):
    a.append(li[i]//10)
    b.append(li[i]%10)
s=b[::-1]
for i in range(len(s)):
    print(a[i],b[i],sep='',end=' ')'''


'''r,c=map(int,input().split())
matrix=[[int(val) for val in input().split()] for i in range(r)]
print('* '*(c+2))
for i in range(r):
    print('*',end=' ')
    for j in range(c):
        print(matrix[i][j],end=' ')
    print('*')
print('* '*(c+2))'''


'''s=input().strip()
n=int(input())
a='abcdefghijklmnopqrstuvwxyz'
ch=a[n-1]
for i in s:
    if i==ch:
        print("yes")
        exit()
print("no")'''

'''s=input().strip()
n=int(input())
val=(len(s)-n)//2
print(s[:val]+s[val:val+n][::-1]+s[val+n:])
'''



'''
# acknowledgement   ->15
# 7
# acknegdelwment
s=input().strip() #acknowledgement
n=int(input())    #7
val=(len(s)-n)//2  #4
print(s[:val]+s[val:val+n][::-1]+s[val+n:]) #acknegdelwment
'''

'''# Your code below
s = input().strip()
if (len(s) % 2 != 0):
    k = (len(s) + 1) // 2
else:
    k = len(s) // 2
start = 0
end = 1
for i in range(k):
    end = start
    start += (i + 1)
    m = s[end:start]
    if (len(m) == 0):
        exit()
    if (len(m) != i + 1):
        m += ('*' * ((i + 1) - len(m)))

    print(' '.join(m[::-1]))'''


'''
n=input().strip()
l=len(n)//2-1
k=[]
for i in range(len(n)//2):
    a=n[i]+'*'*l+n[-1-i]
    print(a)
    l-=1
    k.append(a)
print(n[i+1])
print(*[i for i in k[::-1]],sep='')
'''

# 2,5,4,9
# 4,10
'''
a,b,c,d=map(int,input().split())
x,y=map(int,input().split())
odd= c-a   #2
even=d-b #4
oddnum=c #4   6
evennum=d #9  13
#print(odd,oddnum,even,evennum)
li=[a,b,c,d] #2,5,4,9,6,13,8
for i in range(len(li)+1,y+1):#(5,11)-> i= 5,6,7
    if i%2!=0:
        li.append(oddnum+odd)
        oddnum=li[-1]
        #print("if",oddnum,odd)
    else:
        #print("else",evennum,even)
        li.append(evennum+even)
        evennum=li[-1]
        #print("else2",evennum)
    #print(i,li)
#print(li)
print(*li[x-1:y])
'''


