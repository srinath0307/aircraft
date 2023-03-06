'''
string='animallotsfoliateddetailofstoollamina'
print(len(string))
l=list(string)
j=len(l)-1 #37-1=36;
for i in range(len(l)):
    if(l[i]!=l[j]): #i=8,j=28
        print(l[i],l[j])
        if(l[i]==l[j-1] and i!=j-1):# i=8,j=27
            print(l[i],l[j-1])
            print(l[j])#l[28]=
            break
        else:
            print(l[i])
            break
    j-=1
'''
'''m.n=map(int,input().split())
hr,mi=map(int,input().split(":"))
time=hr*60+mi
ctr=0
li=input().split()
for i in li:
    hr,mi=map(int,i.split(":"))
    t=hr*60+mi
    if time<=t:
        ctr+=1
if (m-ctr)<=n:
    print("YES")
else:
    print("NO")'''


'''
#-4-5
equation=input().strip()
case=int(input())
if case==0:print(eval(equation))
else:
    num1=''
    num2=''
    ch=''
    for j in range(len(equation)):
        if equation[j].isnumeric() or j==0:num1+=equation[j]
        else:
            ch=equation[j]
            num2=equation[j+1:]
            break
    if ch=='+':print(int(num1)-int(num2))
    elif ch=='-':print(int(num1)+int(num2))
    elif ch=='*':print(int(num1)//int(num2))
    elif ch=='/':print(int(num1)*int(num2))'''

'''
a,b,c=map(int,input().split())
for i in range(min(a,c),max(a,c)+1):
    print(i,end=' ')
for i in range(b,max(a,c)-1,-1):
    print(i,end=' ')'''

'''import re
e = input().strip()
sh = int(input())
if sh:
    key = {'+': '-', '-': '+', '*': '//', '/': '*'}
    op = re.findall(r'(?<=\d)[+\-*/]', e)
    print(op)'''
    #e = e.replace(op, key[op])
#print(eval(e))


#1,n ->100
n=100
'''for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')'''
#1,100 -> 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
'''li=[]
for i in range(2,n+1):
    li.append(i)
for i in range(2,n+1):
    for j in range(len(li)):
        if li[j]%i==0 and li[j]!=0 and i!=li[j]:
            li[j]=0
print(li)'''













