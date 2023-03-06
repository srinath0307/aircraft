# 2,5,4,9
# 4,10

'''a,b,c,d=map(int,input().split())
x,y=map(int,input().split())
odd= c-a   #2
even=d-b #4
oddnum=c #4   6
evennum=d #9  13
#print(odd,oddnum,even,evennum)
li=[a,b,c,d] #2,5,4,9,6,13,8
for i in range(len(li)+1,y+1):#(5,11)-> i= 5,6,7
    if i%2!=0:
        li.append(oddnum+odd)
        oddnum=li[-1]
        #print("if",oddnum,odd)
    else:
        #print("else",evennum,even)
        li.append(evennum+even)
        evennum=li[-1]
        #print("else2",evennum)
    #print(i,li)
#print(li)
print(*li[x-1:y])'''

'''
n=int(input())
li=list(map(int,input().split()))
ans=0
for i in li:
    if i%10==0:
        ans=ans+(i/10)
    else:
        ans=ans+(i/(i%10))
print("{:.3f}".format(ans))'''

'''n=int(input())
alphas='abcdefghijklmnopqrstuvwxyz'
asterisk=n-1
print(asterisk*'*'+alphas[0])
ctr=1
asterisk-=1
for i in range(1,n):
    alp=alphas[0:ctr]
    print(asterisk*'*'+alp+alp[::-1][1:])
    asterisk-=1
    ctr+=1
'''

'''
s=list(input().strip())
cons=0;vows=0
for i in range(len(s)-1,-1,-1):
    if s[i] in 'aeiou':
        vows=i
        break
for i in range(len(s)):
    if s[i] not in 'aeiou':
        cons=i
        break
s[vows],s[cons]=s[cons],s[vows]
print(''.join(s))'''