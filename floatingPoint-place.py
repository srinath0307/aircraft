'''s=input().split('.')
placeValue=[int(s[0][ctr])*(10**(len(s[0])-ctr-1)) for ctr in range(len(s[0]))]
for ctr in range(0,len(s[1])):
    if s[1][ctr]=='0':
        placeValue.append(0)
    else:
        placeValue.append(s[1][ctr]+'/'+str(10**(ctr+1)))
print(*placeValue)'''

'''n=int(input())
s=list(map(int,input().split()))
for i in s:
    if i>0:
        print(i*s[i-1],end=" ")
    else:
        print(i*s[-abs(i)],end=" ")
'''

'''s=input().strip()
c=input()
index=len(s)
try:
    index=s.index(c)
except:
    pass
print(s[:index])'''
'''def isValid(S):
    wrongChars = [' ','/']
    specialchars =["@","%","$","*","&","(",")","[","}","]"]
    if len(S) not in range(8,13):
        return False
    if S[0].isdigit():
        return False
    oneNum = 0;oneAlpha = 0;oneCapital = 0;specialChars =0
    for char in S:
        if char in wrongChars:
            return False
        if char.isalpha():
            oneAlpha = 1
        if char.isupper():
            oneCapital = 1
        if char.isdigit():
            oneNum = 1
        if char in specialchars:
            specialChars=1
    if(oneNum and oneAlpha and oneCapital and specialChars):
        return True
    return False
s=input().strip()
if isValid(s):
    print("valid")
    exit()
print("invalid")'''
