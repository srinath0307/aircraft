'''n=int(input())
list=[]
for i in range(n):
    a=input()
    list.append(a)
ext=[];name=[]
dict={}
for j in list:
    n,e=j.split(".")
    ext.append(e)
    name.append(n)
    if e not in dict:
        dict[e]=1
    else:
        dict[e]+=1
for e in dict.keys():
    l=[]
    for n in list:
        if n.endswith(e):
            l.append(n)
            li=[]
            for k in l:
                s,d=k.split(".")
                li.append(s)
    print(f'{e}.{"-".join(li)}')
'''

"""
6
addTwoNumbers.c
mybio.txt
primeNumbers.c
profilepic.jpeg
factorial.c
numbers.txt

7
primenumbers.c
alpha.txt
string.py
numbers.txt
primenumbers.java
words.txt
factors.c
"""

