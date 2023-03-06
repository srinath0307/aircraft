r = int(input(" Enter the no of rows : "))
c = int(input(" Enter the no of columns : "))
x = []
val = []
for i in range(0, r):
    for j in range(0, c):
        val.insert(j, int(input(" enter the %d * %d element " % (i, j))))
    x.insert(i, val)
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
print(sum)