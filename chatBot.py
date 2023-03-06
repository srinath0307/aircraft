'''n1=input()
n2=input()
number1=0;number2=0
if len(n1)>len(n2):
    number2=n2.zfill(len(n1))
    number1=n1
else:
    number1 = n1.zfill(len(n2))
    number2=n2
ctr=len(number1)-1
carry=0
count=0
while ctr>0:
    summ=str(int(number1[ctr])+int(number2[ctr])+carry)
    if len(summ)>=2:
        carry=int(summ[0])
        count+=1
    ctr-=1
print(count)
'''
'''x=int(input())
y=int(input())
count=0;carry=0
while x>0 or y>0:
    carry=x%10+y%10+carry
    if carry>9:
        count+=1
        carry=1
    else:
        carry=0
    x//=10
    y//=10
print(count)'''
s=input().strip()
print(s[0])
for i in range(1,len(s)-1):
    if s[i]=="{":
        for j in range(i):
            print("\t")
            print(s[i])
            break
    else:
        for j in range(i):
            print("\t")
            print(s[i])
print(s[-1])
#{{{}}{}}