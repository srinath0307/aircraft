# Your code below
n = int(input())
s = str(n)
k = []
y = []
for i in s:
    y.append(int(i))
for i in range(len(s)):
    k.append(0)
u = 0
while (1):
    if k == y:
        print(*k, sep="")
        break
    if k[u] == y[u]:
        u += 1

    else:
        print(*k, sep="")
        k[u] = k[u] + 1

n = [int(i) for i in input().strip()]
l = [0] * len(n)
print(*l, sep="")
for i in range(len(n)):
    for j in range(1, n[i] + 1):
        l[i] = j
        print(*l, sep="")
