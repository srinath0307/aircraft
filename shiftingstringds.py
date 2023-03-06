'''words=[val for val in input().split()]
shift=int(input())
count=0
revisedword=[]
for word in words:
    l=shift%len(word)
    newword=word[-l:]+word[:-l]
    revisedword.append(newword)
    if newword==word:
        count+=1
print(count)
print(*revisedword)'''
''' 
tiger spider
5
'''
'''n=int(input())
li=list(map(int,input().split()))
evenlist=[]
for num in li:
    if num%2==0:
        evenlist.append(num)
if len(evenlist)==0:
    print("-1")
else:
    print(*evenlist[::-1])'''
'''n=int(input())
li=list(map(int,input().split()))
flag=False
for num in li[::-1]:
    if num%2==0:
        flag=True
        print(num,end=" ")
if flag==False:
    print("-1")'''
'''ch=input()
if ch=='a':
    print('z',chr(ord(ch)+1),sep="")
elif ch=='z':
    print(chr(ord(ch)-1),'a',sep="")
else:
    print(chr(ord(ch)-1),chr(ord(ch)+1),sep="")'''

