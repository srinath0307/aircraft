from itertools import permutations
N = str(int(input()))
for length in range(len(N),0,-1):
    lenComb = []
    for order in permutations(N,length):
        comb = ''.join(order)
        if comb not in lenComb:
            lenComb.append(comb)
    print(*lenComb,sep=",")