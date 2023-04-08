'''s = input().strip()
s = s.split('//')
print(s)
s = ''.join(s[1:])
s = s.split('/')
k = s[0][::-1].index('.')
k = len(s[0]) - k
print(s[0][k - 1:])'''

'''
https://www.skillrack.com/solve/8464
'''

# dynamic v pattern
# Path: dynamicVpattern.py
'''x, c, y = input().split()
x = int(x)
y = int(y)
m = []
for i in range(1, y + 1):
    if y - x >= i or i == y:
        m.append('-' * (y + x - 1 - i) + c)
    else:
        m.append('-' * (i - (y - x) - 1) + c + '-' * (2 * (y - i) - 1) + c)
for i in range(0, x - y):
    print('-' * i + c)
print(*m, sep='\n')
'''

'''s=input().strip()
for i in range(1,len(s)-1):
    if s[i]=='*':
        if s[i-1]!=s[i+1]:
            print("no")
            exit()
print("yes")'''

'''s = "skillrack"
li = []
for i in s:
    if i not in li:
        li.append(i)
    else:
        li.remove(i)
if li:
    print(s.index(li[0]))
else:
    print("-1")'''

# m=int(input())
# n=int(input())
# z=0
# for i in range(m,n+1):
#     if i%2==0:
#         z+=1
# print(z)

'''s=input().strip()
l=[]
for i in s:
    l.append(i)
phx=0
for i in l:
    if int(i)%2!=0:
        phx+=int(i)
print(phx)'''

'''l1 = []
l2 = []
for i in range(11, 25):
    if i % 2 != 0:
        l1.append(i)
    else:
        l2.append(i)
l2 = l2[::-1]
for i in range(min(len(l1), len(l2))):
    print(l1[i], l2[i], end=' ')
if len(l1) > len(l2):
    print(l1[-1])
elif len(l1)<len(l2):
    print(l2[-1])
'''