'''s=input().split()
for i in s:
    for j in range(len(i)):
        if (j+1)%2!=0:
            print(i[j].upper(),end='')
        else:
            print(i[j].lower(),end='')
    print(end=' ')
'''

'''
max_sum=0
for row in range(r-1):
    for col in range(c-1):
        summation=mat[row][col]+mat[row][col+1]+mat[row+1][col]+mat[row+1][col+1]
        if summation>max_sum:
            max_sum=summation
print(max_sum)'''
'''
n=int(input())
ctr=n
for i in range(1,n+1):
    for j in range(ctr,n+1):
        print(j,end='')
    print(0,end='')
    for j in range(n,ctr-1,-1):
        print(j,end='')
    ctr-=1
    print()'''


#thunderCodes;
'''from itertools import permutations
N = input().strip()
if int(N)%8 == 0:
    print("Yes")
    exit()
for comb in permutations(N[-3:],3):
    if int(''.join(comb))%8 == 0:
        print("Yes")
        exit()
print("No")'''


'''s=input().strip()
li=[int(i) for i in s]
if li[1]%2==0:
    print(li[0])
for i in range(1,len(li)):
    if li[i+1]%2==0 and li[i-1]%2==0:
        print(li[i])
if li[-2]%2==0:
    print(li[-1])'''



'''
n=int(input())
summ=0 
ctr=1 
while ctr<=n:
    summ+=(ctr*ctr*ctr)
    ctr+=1
print(summ)'''


'''import time
import threading
start = time.time()
for i in range(10**7):
    print(i)
print(time.time()-start)'''


#1000999998997996  ->1000
#1000999997  -> -1