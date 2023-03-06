'''s=input().strip()
li=[]
out=[]
for i in s[::-1]:
    if i not in li:
        li.append(i)
        k="{}{}".format(i,1)
        out.insert(0,k)
    else:
        li.append(i)
        out.insert(0,"{}{}".format(i,li.count(i)))
print(*out)'''
#google
#hippopotamus

'''n=int(input())
li=[int(val) for val in input().split()]
x=int(input())
ctr=0
main=[]#bargraph
while ctr<n:
    listt=[]
    for k in range(max(li)-li[ctr]):
        listt.append("-"*x)
    for l in range(li[ctr]):
        listt.append("*"*x)
    main.append(listt)
    ctr+=1
kk=0
while kk<len(main[0]):
    for i in range(len(main)):
        print(main[i][kk],end="")
    print()
    kk+=1'''
'''
6
5 4 8 3 1 4
2
'''
'''a,b=map(int,input().split())
l=[list(map(int,input().split())) for i in range(a)]
x,y=[int(i)-1 for i in input().split()]
for i in range(y,b):
    print(l[x][i],end=' ')
for i in range(x+1,a):
    print(l[i][-1],end=' ')
for i in range(b-2,y-1,-1):
    print(l[-1][i],end=' ')
for i in range(a-2,x,-1):
    print(l[i][y],end=' ')'''















