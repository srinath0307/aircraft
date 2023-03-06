'''class Date:
    def __init__(self,year,month="Jan",day="01"):
        self.year = year
        self.month = month
        self.day=day
    def __str__(self):
        return "{}-{}-{}".format(self.day,self.month,str(self.year).zfill(4))
day=int(input())
month=input().strip()
year=int(input())
date1=Date(year)
date2=Date(year,month)
date3=Date(year,month,day)
print(date1)
print(date2)
print(date3)
"""
8
nov
985
"""'''
'''def maximum(num):     
    i=1
    max=num%10
    ctr=num
    while i<len(str(num)):
        ctr=(ctr//10)%10
        if ctr>=max:
            max=ctr
        i+=1
    return max
n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))
maxli=[]
for i in list:
    a=maximum(i)
    maxli.append(a)
sum=0
for i in maxli:
    sum+=i
print(sum)'''
'''while True:
    try:
        line=input().split()
        for word in line:
            print("{}{}".format(word,len(word)),sep="",end=" ")
        print()
    except:
        break'''


'''l1=[]
for i in range(1000):
    try:
        a=input().strip().split()
        if a!="\n":
            l1.append(a)
        else:
            break
    except:
        break
for i in l1:
    for j in i:
        print(j,len(j),sep="",end=" ")
    print()'''
'''r,c=map(int,input().split())
matrix=[input().split() for r in range(r)]
print(matrix)
intlist=[]
wordlist=[]
for col in range(c):
    if matrix[0][col].isdigit():
        num=0
        for row in range(r):
            num=num+int(matrix[row][col])
        intlist.append(num)
    else:
        s=""
        for row in range(r-1,-1,-1):
            s+=matrix[row][col]
        wordlist.append(s)
print(*intlist,*wordlist)'''
"""
4 5
a 10 r e 8
b 20 a n 7
c 30 c o 6
d 40 k n 50
"""
'''import re
s=input()
numlist=re.findall("[0-9]+",s)
strlist=re.findall("[a-zA-Z]+",s)
print(strlist)
print(numlist)
a=[]
for i in range(len(numlist)):
    a.append(strlist[i:]*int(numlist[i]))
for i in a:
    print(*i,sep="")'''

'''n=int(input())
print('*'*(n*2+1))
ctr=1
for i in range(1,n*2+2):
    if i%2!=0:
        print('*',end='')
    else:
        print(ctr,end='')
        ctr+=1
print()
print('*'*(n*2+1))'''