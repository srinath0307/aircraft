'''s=input().strip()
if '_' not  in s:
    print(s[::-1])
    exit()
if s.index('_')==0:
    print(s)
    exit()
ind=s.index('_')
print(s[:ind][::-1],s[ind:],sep='')'''
'''#n=1290.12
rupeee,paise=map(int,input().split('.'))
print(rupeee*100+paise)'''
'''n=int(input())
li=[int(input()) for _ in range(n)]
main=[]
for i in li:
    for j in range(2,i+1):
        if i%j==0:
            main.append(j)
print(main)
ctr=0
for i in main:
    if main.count(i)==len(li):
        print(main.count(i),len(li),i)

        ctr+=1
print(ctr)
print(ctr//n)'''
#li=list(range(1,11))
'''input1='zx:za:ee'
alpha=[chr(i) for i in range(ord('a'),ord('z')+1)]
alpha.insert(0,0)
print(alpha)
s=input1.split(":")
ss=''
for i in s:
    if i[0]==i[1]:
        ss+=i[0]
    else:
        a=abs(alpha.index(i[0])-alpha.index(i[1]))
        ss+=alpha[a]
print(ss.upper())'''









'''input1=['G','Q','R']
input2=['R','U','T']
a=[]
for i in input1:
    if i not in input2:
        a.append(ord(i))
for i in input2:
    if i not in input1:
        a.append(ord(i))
a=list(set(a))
#print(a)
tot=sum(a)
while len(str(tot))>1:
    t=0
    for i in str(tot):
        t+=int(i)
    tot=t
print(tot)'''

'''input1=2
input2=20
s=''
for i in range(0,input2+1):
    s+=str(i)
print(s.count(str(input1)))'''
'''input1='fruits'
inpit2='are good'
input1=input1.strip().split()
inpit2=inpit2.strip().split()
input1=''.join(input1)
inpit2=''.join(inpit2)
if input1=='' or inpit2=='':
    print("null")
s=sorted(list(set(list(input1+inpit2))),reverse=True)
print(''.join(s))'''




'''input1=3
input2=['oreo','sirish','apple']
ans=''
vowels='aeiouAEIOU'
for i in input2:
    if i[0] in vowels and i[-1] in vowels:
        ans+=i
if ans!='':
    print(ans.lower())
else:
    print("no matches found")'''


'''input1='Wipro'
input2=0
s=''
if input2==0:
    for i in range(len(input1)):
        if i%2==0:
            if input1[i].isupper():
                s+=input1[i].lower()
            else:
                s+=input1[i].upper()
    print(s)
elif input2==1:
    for i in range(len(input1)):
        if i%2!=0:
            if input1[i].isupper():
                s+=input1[i].lower()
            else:
                s+=input1[i].upper()
    print(s)
else:
    for i in input1:
        if i.isupper():
            s+=i.lower()
        else:
            s+=i.upper()
    print(s[::-1])'''

'''
a,b=input().split()
a=int(a)
b=int(b)
li=[]
for i in range(a,b+1):
    li.append(i)
while li[0]!=b:
    print(*li)
    d=li.pop(0)
    li.insert(b-a,d)
print(*li)'''





'''
for i in input1:
    if i in [' ','(',')','!','@','#','$','%','*']:
        return 1
return ord(input1[0])+ord(input1[-1])
    '''


'''input1='lLQwfg'
input2='QwlLkfg'
s=''
l1=[]
l2=[]
ctr=0
for i in input1:
    l1.append(ord(i))
for j in input2:
    l2.append(ord(j))
if sorted(l1)==l1:
    s='Increasing'
elif sorted(l1,reverse=True)==l1:
    s='Decreasing'
if s=='':
    print("invalid")
for i in range(len(input1)):
    if input1[i]!=input2[i]:
        ctr+=1
print("{}:{}".format(s,ctr))'''





'''input1=[6,7,12,70,44]
input2=[8,6,70,44]
total=0
for val in input1:
    if val not in input2:
        total+=val
for val in input2:
    if val not in input1:
        total+=val
while len(str(total))>1:
    s=0
    for i in str(total):
        s+=int(i)
    total=s
print(total)
'''

'''s='REQUEST'
s=list(s)
if len(s)%2!=0:
    for i in range(len(s)):
        if i%2!=0:
            s[i]=''
else:
    for i in range(len(s)):
        if i%2==0:
            s[i]=''
s=[i for i in s if i!='']
print(''.join(s))'''


'''input1=['a','b','c']
input2=['b','c']
li=[]
for i in input2:
    if i in input1:
        li.append(i)
for i in input1:
    if i in input2:
        li.append(i)
li=list(set(li))
li=[ord(i) for i in li]
total=sum(li)
while len(str(total))>1:
    s=0
    for i in str(total):
        s+=int(i)
    total=s
print(total)'''


'''input1=5
factorial=1
if input1==1:
    print(1)
else:
    for i in range(1, input1 + 1):
        factorial = factorial * i
print(factorial)'''
'''return input1%10+input2%10'''

'''
input1='wipro'
vowels='aeiouAEIOU'
ans=''
for i in input1:
    if i in vowels:
        ans+=i
print(ans)'''



'''n=int(input())
li=list(map(int,input().split()))
a=[]
for i in li:
    if i%2==0 and i%3==0:
        a.append(i)
print(*a)'''




'''n=int(input())
strings=[]
for i in range(n):
    s=input().strip()
    strings.append(s)
l=len(strings)-1
sample=''
for index in range(l,-1,-1):
    sample+=l[index]
print(sample)'''

'''s='manager'
index=0
for i in range(len(s)-1,-1,-1):
    if s[i] in 'aeiou':
        index=i
        break
print(index)
s=s[:index+1][::-1]+s[index+1:]
print(s)'''



'''s=input().strip()
index=0
for i in s:
    if s[i] in 'aeiou':
        index=i
        break
#index=5
print(s[0:index+1][::-1],s[index+1:],sep='')
'''
'''n=int(input())
li=list(map(int,input().split()))
while len(li)>1:
    o=[]
    for i in range(len(li)-1):
        o.append(li[i]+li[i+1])
    #print(o)
    li=o
#print(li)
y=li[0]
while len(str(y))>1:
    u=0
    for i in str(y):#'12'
        u+=int(i)
    y=u
print(y)'''
#li=[1,2,3,4,5]
#li=[3,5,7,9]
#li=[8,12,16]
# 48 ->12-> 3\






'''a=[1,2,3,4,5]
x=[]
while(len(a)>1):
    for i in range(len(a)-1):
        x.append(a[i]+a[i+1])
    a.clear()
    a=x.copy()
    x.clear()
print(a)
y=a[0]
while len(str(y))>1:
    u=0
    for i in str(y):#'12'
        u+=int(i)
    y=u
print(y)'''


'''n=int(input())
li=list(map(int,input().split()))
for i in range(n-1):
    if not abs(li[i]-li[i+1])==1:
        print("no")
        exit()
print("yes")'''

'''li1=[1,2,3,4,5,3,3,4]
li2=[2,4,7,6,5,4,8,8,3,6,2,3]
new_li=[]
for i in li2:
    if i in li1 and i not in new_li:
        new_li.append(i)
print(new_li)'''








