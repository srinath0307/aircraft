n = int(input())
pair = []
for i in range(n):
    l, b = map(int, input().split())
    pair.append([l, b])
print(pair)
area = []
for i, j in pair:
    value = i * j
    area.append(value)
print(area)
liist = []
x = 0
while (x < len(pair) - 1):
    for i, j in pair:
        r = [i, j, area[x]]
        liist.append(r)
        x += 1
print(liist)
so = sorted(liist, key=lambda x: (x[2], x[1]), reverse=True)
print(so)
