'''s1=input().strip()
s2=input().strip()
stack,maxdepth,maxdepthIndex=[],0,0
for index in range(len(s1)):
    if s1[index]=='(':
        stack.append(s1[index])
    else:
        if len(stack)>maxdepth:
            maxdepth=len(stack)
            maxdepthIndex=index
        stack.pop()
print(s1[:maxdepthIndex]+s2+s1[maxdepthIndex:])'''
''' 
()(()(()))((()))(()()())
(()(())())                  
'''
matrix=[input().strip() for row in range(4)]
for i in zip(*matrix):
    binstr="".join(i)
    if " " in binstr:
        print(":",end="")
    else:
        print(int(binstr,2),end="")
''' 
00 00 00
00 10 00
10 00 00
00 01 01
'''
