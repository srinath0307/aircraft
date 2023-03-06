'''r = int(input(" Enter the no of rows : "))
c = int(input(" Enter the no of columns : "))
x = []
val = []                  #[1,2]
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input(" enter the %d * %d element " % (i, j))))
        #print(val)
    x.insert(i, val)
    print(x)
    val = []

y = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input(" enter the %d * %d element " % (i, j))))
    y.insert(i, val)
    val = []

sum = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i, val)
    val = []
print(sum)'''

'''n=int(input())
li=[bin(int(val))[2:] for val in input().split()]
l=[i[1:]+i[0] for i in li]
for i in l:
    print(int(i,2),end=" ")'''





n=int(input())
li=list(map(int,input().split()))
sumli=sum(li)
for i in range(1,101):
    if sumli<=2**i:
        print(2**i)
        exit()













