'''s=input().strip()
level=0
num=0
sum=0
for i in s:
    if i=='(':
        if num!=0:
            sum+=num*level
        num=0
        level+=1
    elif i==')':
        if num!=0:
            sum+=num*level
        num=0
        level-=1
    else:
        num=num*10+int(i)
print(sum)'''
''' 
((((10)20)30)40) 
'''
''' 
4(((1)2(3)4)(5)6)
'''
'''a,b,c,d,e=map(int,input().split())
d+=c
if d>a:
    e=a-d
else:
    d+=c
if e<d:
    print(e)
    exit()
else:
    e=d-b
print(e)
'''



hr,mi=map(int,input().split(':'))
Time=hr*60+mi
times=input().split()
count=0
for t in times:
    h,m=map(int,t.split(':'))
    ti=h*60+m
    if ti>Time:
        count+=1
print(count)