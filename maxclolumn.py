'''r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(list(map(int, input().split())))
matrix = [list(i) for i in zip(*matrix)]
matrix = sorted(matrix, key=lambda x: max(x))
matrix = [list(i) for i in zip(*matrix)]
for i in range(r):
    print(*matrix[i])
'''

'''s = input().strip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
consonants = 'bcdfghjklmnpqrstvwxyz'

if s == 'z':
    print('z', end='')
    t = 0
else:
    t = alphabet.index(s) + 1
print(t)
while alphabet[t] != s:
    print(t,"dh")
    print(alphabet[t])
    if t > 25:
        t = 0
    else:
        t += 1
'''

f = 0
s = input().strip()
for i in s:
    if i.isalnum():
        print(i, end='')
    else:
        if f == 0:
            print('.', end='')
            f = 1
        else:
            print(',', end='')
            f = 0
