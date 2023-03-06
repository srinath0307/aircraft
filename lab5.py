s=input().strip()
pairs={"(":")","{":"}","[":"]"}
stack=[]
for i in s:
    if i in "([{":
        stack.append(i)
    else:
        if stack==[]:
            print("no")
            exit()
        closed=i
        opened=stack.pop()
        if pairs[opened]!=closed:
            print("no")
            exit()
if stack==[]:
    print("yes")
else:
    print("no")








