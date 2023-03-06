'''n=int(input())
a=[]
for i in range(n):
    s,e=input().split()
    h,m=map(int,s.split(':'))
    m1=h*60+m
    h,m=map(int,e.split(':'))
    m2=h*60+m
    a.append([m1,m2])
a.sort()
end=0
for s,e in a:
    if end>s:
        print("NO")
        quit()
    end=e
print("YES")'''


"""

#Your code below
n=int(input());a=[]
for i in range(n):
    l=list(map(str,input().split()))
    a.append(l)
a=sorted(a,key=lambda x:x[0])
for i in range(n-1):
    if a[i][1]>a[i+1][0]:
        print('NO')
        exit()
print('YES')"""
"""
#thunderCodes;
allTime = [0 for _ in range(1441)]
N = int(input())
for ctr in range(N):
    start , end = map(str,input().split())
    startH , startM = map(int,start.split(":"))
    endH , endM = map(int,end.split(":"))
    for i in range(startH*60+startM,endH*60+endM):
        if allTime[i] == 1:
            print("NO")
            exit()
        else:
            allTime[i] = 1
print("YES")"""
"""
#Your code below
n = int(input())
l = sorted([input().split() for i in range(n)])
for i in range(1, n):
    if l[i-1][1] > l[i][0]:
        print("NO")
        break
else:
    print("YES")"""
class List:
    def __init__(self):
        self.items=[]
        self.numitems=0
    def append(self,items):
        self.items.append(items)
        self.numitems=self.numitems+1
    def getitems(self):
        return self.items
    def setitems(self,index,value):
        self.items[index]=value
l=List()
l.append(45)
l.append([1,2,3])
print("initially:",l.getitems())
l.setitems(1,[11,22,33,44,55])
print("after setting:",l.getitems())
print("the number of items in your list:",l.numitems)
print("")
