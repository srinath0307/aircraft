'''n=input().strip()
numbers,words=[],[]
i=0
while i<len(n):                                       #9
    if n[i].isdigit():
        j=i
        while j<len(n) and n[j].isdigit():
            j+=1
        numbers.append(int(n[i:j]))
        i=j
    else:
        j=i
        while j<len(n) and n[j].isalpha():
            j+=1
        words.append(n[i:j])
        i=j
for i in range(len(numbers)):
    for j in range(numbers[i]):
        print(*words[i:],end=" ")
    print()
"""4hi5hello
hi hello hi hello hi hello hi hello
hello hello hello hello hello """'''
'''num=int(input())
for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")'''
'''class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.totalpages=None
        self.gener=None
        self.totalchapters=None
    def __del__(self):
        pass
    def addInfo(self,totalpages=None,totalchapters=None):
        self.totalpages=totalpages
        self.gener=gener
        self.totalchapters=totalchapters
    def getInfo(self):
        self.info={}'''

'''import sys
class MinHeap:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.size=0
        self.heap=[0]*(self.maxsize+1)
        self.heap[0]=-1*sys.maxsize
        self.FRONT=1
    def parent(self,pos):
        return pos//2
    def leftchild(self,pos):
        return 2*pos
    def rightchild(self,pos):
        return (2*pos)+1

    def isleaf(self,pos):
        if pos>=(self.size//2) and pos<=self.size:
            return True
        return False
    def swap(self,fpos,spos)
        self.heap[fpos],self.heap[spos]=self.heap[spos],self.heap[fpos]
    def minheapify(self,fpos):
        if not self.isleaf(pos):
            if (self.heap[pos]>self.heap[self.leftchild(pos)]) or self.heap[pos]>self.heap[]'''
'''n=int(input())
arr=list(map(int,input().split()))
k=int(input())
for index in range(0,k):
    for subind in range(k,n):
        arr[subind]+=arr[subind]%arr[index]
print(*arr)'''
'''s=input()
l=[val for val in s]
vowels=['a','e','i','o','u']
for i in range(0,len(s)-1,2):
    if l[i] and l[i+1] not in vowels:
        l[i],l[i+1]=l[i+1],l[i]
print(*l,sep="")
#introduction'''