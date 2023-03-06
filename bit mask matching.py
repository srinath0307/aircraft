n=int(input())
s=input().strip()
binN=bin(n)[2:].zfill(26)
alphas=[chr(i) for i in range(97,123)]
flag=False
for letter in s:
    a=alphas.index(letter.lower())
    if str(binN)[::-1][a]=='1':
        flag=True
    else:
        flag=False
if flag:
    print("YES")
else:
    print("NO")


''' 
44
DECADE    #0000000000000001010   01010000000000000000
'''
""" 
10 
BDBB         
"""