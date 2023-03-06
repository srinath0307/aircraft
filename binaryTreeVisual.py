'''
#Your code below
n=int(input())
li=[input().strip() for _ in range(n)]
start=''
for i in li:
    flag=0
    for j in li:
        if i!=j:
            if i[0]==j[-1]:
                flag=1
                break
    if flag==0:
        start=i
        break
ctr=1
print(start)
while ctr<=n:
    for i in li:
        if start[-1]==i[0]:
            print(i)
            start=i
            break
    ctr+=1'''
'''
4
orange
pancrea
neuro
amazon
'''







'''res=[]
for i in salesRecord:
    res.append(max(i))
return res
'''

'''
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
    if size1 != size2:
        return -1
    temp = string1 + string1
    if (temp.count(string2) > 0):
        return 1
    else:
        return -1'''
'''parent='timisplayinginthehouseoftimwiththetoysoftim'
sub='tim'
ctr=0
for i in range(0,len(parent),len(sub)):
    if parent[i:i+len(sub)]==sub:
        ctr+=1
        #print(parent[i:i+len(sub)])
print(ctr)
print(parent.count(sub))
'''

'''inputArr=[10,98,3,33,12,22,21,11]
oddli=[];evenli=[]
for i in inputArr:
    if i%2==0:
        evenli.append(i)
    else:
        oddli.append(i)
return evenli+oddli
'''
'''currentState=[1,1,1,0,1,1,1,1]
days=2
for i in range(days):
    newli=[0]
    for j in range(1,len(currentState)-1):
        if currentState[j-1]==1 and currentState[j+1]==1:
            newli.append(0)
        else:
            newli.append(1)
    print(currentState,newli)
    currentState=newli
print(currentState)
'''

'''n=int(input())
matrix=[]
ctr=1
for i in range(n):
    sub=[]
    for j in range(n):
        sub.append("*")
    matrix.append(sub)
for i in range(1,n-1):
    for j in range(1,n-1):
        matrix[i][j]=ctr
        ctr+=1
matrix[n//2][n//2]='*'
for i in matrix:
    print(*i)'''


'''orderPlaced=[-11,-2,19,37,64,-18]
size=3
l=[]
for i in range(0,len(orderPlaced)):
    if len(orderPlaced[i:i+size])==size:
        if min(orderPlaced[i:i+size])<0:
            for j in orderPlaced[i:i+size]:
                if j<0:
                    l.append(j)
                    break
        else:
            l.append(0)
#return l'''



#print(pow(pow(secretcode,firstkey)%10,secondkey)%100000
'''ctr=0
for i in range(0,len(req),2):
    ctr+=req[i]
print(ctr)'''
#print(sum(req[::2]))






'''key=756
li=sorted([int(i) for i in str(key)])
tot=0
for i in li:
    tot=tot*10+i
print(tot)
'''


'''textInput='aa a234bc@ sad$ hsagd^'
ctr=0
for i in textInput:
    if i.isalpha() or i.isnumeric() or i==' ':
        pass
    else:
        ctr+=1
print(ctr)'''




















