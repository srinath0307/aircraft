s1=input().strip()
s2=input().strip()
lii=sorted(s1,key=lambda x: s2.index(x))
print(*lii,sep="")
"""
1358719
0219487563
"""
"""
#Your code below 
m=input().strip() 
n=input().strip() 
for i in n:                           0219487563
    for j in m:                       1358719
        if j==i: 
            print(j,end="")
"""
""" 
s1=input().strip()
s2=input().strip()
for i in s2:
    if i in s1:
        print(s1.count(i)*i,end="")

"""

