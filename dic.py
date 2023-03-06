'''x=8
y=3
li=[3,8,3,8,3,4,5,8,3]
d={}
for i in li:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
o=[]
for i in d:
    o.append([i,d[i]])
print(o)
o=sorted(o,key=lambda x:(x[1],x[0]))
print(o)'''

'''s=input().strip().split('#')
print(s)
for i in range(1,len(s)-1):
    print(s[i],end='')
'''
'''
a, b = input().split()
a = list(a)
b = list(b)
a[-1], b[-1] = b[-1], a[-1]
print(int(''.join(a)) * int(''.join(b)))
'''