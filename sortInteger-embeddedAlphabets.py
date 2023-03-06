n=int(input())
list=[val for val in input().split()]
def alpha(x):
    val=""
    for i in x:
        if i.isalpha():
            val=val+i
    return val
def num(x):
    number=""
    for i in x:
        if i.isnumeric():
            number=number+i
    return int(number)
sorlist=sorted(list,key=lambda x:(alpha(x),num(x)))
finaList=[]
for i in sorlist:
    numb=""
    for j in i:
        if j.isnumeric():
            numb+=j
    finaList.append(numb)
print(*finaList)

'''
4
984b b14 20c0 662a
5
12e2 98e e354 2e5 89e1
'''