'''n=int(input())
l=[['-' for j in range(n**2)]for i in range(n**2)]
for i in range(0,n**2,n):
    for j in range(0,n**2,n):
        for ii in range(n):
            l[ii+i][j+ii]='*'
for i in l:
    print(*i)'''

'''num=int(input())
items=[int(val) for val in input().split()]
ctr=0
li=[]
for val in items:
    if val%2==0:
        li.append(val)
        items.remove(val)
for i in items:
    if i+1 in li:
        ctr+=1
        li.remove(i+1)
print(ctr)'''
'''s1=input().strip()
s2=input().strip()
li=[]
for i in s2:
    if i not in s1:
        print("No")
        exit()
    li.append(s2.count(i))
lis=list(set(li))
for i in lis:
    if len(lis)==1 and len(s1)==1:
        print("yes")
        exit()
print("yes")'''
'''class Student:
    def __init__(self,ram,ravi):
        self.ram = ram
        self.ravi = ravi

    def marks(self):
        print("The maths marks are : ",self.ram,self.ravi)
        print("The science marks are : ",self.ram,self.ravi)
s1 = Student(80,95)
s2 = Student(90,86)

s1.marks()
s2.marks()'''



