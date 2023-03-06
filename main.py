'''s1 = list(input().strip())
s2 = list(input().strip())
score = 0
for i in range(min(len(s1), len(s2))):
    if s1[i] == s2[i]:
        score += 2
        s1[i] = "*"
        s2[i] = "*"
for index1 in range(len(s1)):
    for index2 in range(len(s2)):
        if s2[index2] != "*" and s1[index1] == s2[index2]:
            score += 1
            s2[index2] = "*"
            break
print(score)'''
''' 
bhuvana
lavanya 
'''
'''s=input()
chararr=[chr(i) for i in range(97,123)]
for i in s:
    if chararr.index(i.lower())%2==0:
        print(1,end="")
    else:
        print(0,end="")'''

'''a=[]
n=int(input("Enter the value of n"))
for i in range(0,n):
    x=int(input())
    a.append(x)
print(a)
for i in range(0,n):
    s=min(a[i:])
    isa=a.index(s)
    a[i],a[isa]=a[isa],a[i]
print("Sorted order is")
print(a)'''

'''

s=input().strip()   #   14a5b
num=''  #
numbers=[]
alphabets=[]
for i in s:
    if i.isdigit():
        num+=i
    else:
        numbers.append(int(num))
        num=''
        alphabets.append(i)
for i in range(len(numbers)):
    print(numbers[i]*alphabets[i],end='')


'''

'''n=input().strip()
a=int(input())
b=int(input())
c=int(n,a)
print(c)
i=1
while i:
    if len(str(i))>len(str(b)):
        if (i//10%10)* (i%10) == b:
            print(i)
            break
    else:
        if i%10 == b:
            print(i)
            break
    i+=1
# 9 is represented with base 10 as 9

'''
'''
n = '534632'
odd = [i for i in n if int(i) % 2 != 0]  # [5,3,3]
even = [i for i in n if int(i) % 2 == 0]  # [4,6,2]
oddInd = 0
evenInd = 0
for i in n:
    if int(i) % 2 == 0:
        print(odd[oddInd], end='')
        oddInd += 1
    else:
        print(even[evenInd], end='')
        evenInd += 1'''

'''ch = input().strip()
if ch.islower():
    z = 'z'
else:
    z = 'Z'


def isconsonant(ch):
    if ch not in 'AEIOUaeiou':
        return True
    else:
        return False


for i in range(ord(ch) + 1, ord(z) + 1):
    if isconsonant(chr(i)):
        print(chr(i))
        break'''




















