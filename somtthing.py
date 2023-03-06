'''n=int(input())
li=[val for val in input().split()]
ctr=0
limerge=[]
while ctr<len(li):
    limerge.append(li[ctr]+li[ctr+1])
    ctr+=2
print(limerge)'''
'''s1='31937902903'
s2='28736910793'
def order(s):
    li=[]
    for i in s:
        li.append(s2.index(i))
    return li
s1=sorted(s1,key=lambda x:order(x))
print(*s1,sep="")'''

'''n=int(input())
numbers=list(map(int,input().split()))  #[int(val) for val in input().split()]   #[12 14 56 14 14]
count=0
for num in numbers:
    if numbers[len(numbers)-1]==num:
        count=count+1
print(count)'''
n=int(input())
ctr=5
while ctr>0:    #5
    n+=n
    ctr-=1
print(n)