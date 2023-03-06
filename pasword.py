password=input().strip()
smallchar=[chr(i) for i in range(97,123)]
num=[i for i in range(0,10)]
capitalchar=[chr(i) for i in range(65,91)]
specialchar=["@","!","#","$","%","^","*"]
flag=False
if len(password)>=8 and len(password)<=12:
    flag=True
elif password[0].isnumeric():
    print("invaid")
    exit()
else:
    print("invalid")
    exit()
for val in password:
    if val in smallchar:
        flag = True
    if val in capitalchar:
        flag = True
    if val in num:
        flag = True
    if val in specialchar:
        flag=True
if flag:
    print("valid")
else:
    print("invaid")
'''def isValid(S):
    wrongChars = [' ','/']
    if len(S) not in range(8,13):
        return False
    if S[0].isdigit():
        return False
    oneNum = 0;oneAlpha = 0;oneCapital = 0
    for char in S:
        if char in wrongChars:
            return False
        if char.isalpha():
            oneAlpha = 1
        if char.isupper():
            oneCapital = 1
        if char.isdigit():
            oneNum = 1
    if(oneNum and oneAlpha and oneCapital):
        return True
    return False
a=input().strip()
b=isValid(a)
if b:
    print("valid")
    exit()
print("invalid")'''
''' 
Z1assd!k 
'''
'''def isValid():
    S = input("Enter the password").strip()
    wrongChars = [' ','/']
    if len(S) not in range(8,13):
        return False
    if S[0].isdigit():
        return False
    oneNum = 0;oneAlpha = 0;oneCapital = 0
    for char in S:
        if char in wrongChars:
            return False
        if char.isalpha():
            oneAlpha = 1
        if char.isupper():
            oneCapital = 1
        if char.isdigit():
            oneNum = 1
    if(oneNum and oneAlpha and oneCapital):
        return True
    return False

b=isValid()
if b:
    print("Program is valid : ")
else:
    print("Program is invalid : ")'''




