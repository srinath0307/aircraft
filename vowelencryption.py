'''s=input().strip()
vowels='aeiou'
count=0
for i in s:
    if i in vowels:
        count+=1
    else:
        if count==0:
            print(i,end="")
        else:
            print(count,end="")
            count=0'''
'''
kgooooooooooseee
'''
'''s=input().strip()
vowels='aeiou'
for i in s:
    if i not in vowels:
        print(i,end="")
    else:
        count=1
        for j in s[s.index(i):]:
            if j in vowels:
                count+=1
        print(count,end="")'''
'''s=input().strip()
vowels='aeiou'
ctr=0
count=0
for i in s:
    if i not in vowels:
        print(i,end="")
    else:
        count+=1
    print(count,end="")'''
'''s=input().strip()
vowels='aeiou'
for i in s:
    if i not in vowels:
        print(i,end="")
    else:
        count=0
        for j in s[s.index(i):]:
            if j in vowels:
                count+=1
            else:
                print(count,j,end="")'''
'''s=list(input().strip().split())
vowels='aeiou'
count=0
for i in s:
    if i not in vowels:
        print(i)
    else:
        for j in s[s.index(i):]:
            if j in vowels:
                count+=1
                s.pop(s.index(j))
        print(count)'''
'''s=input().strip()
vowels='aeiou'
ctr=0
count=0
for i in s:
    if i not in vowels:
        print(i,end="")
    else:
        count+=1
    print(count,end="")'''




'''def vowelEncryption(str1):
    str2=[]
    for i in range(len(str1)):
        count=0
        if str1[i] in 'aeiou':
            for i in range(i, len(str1)):
                if str1[i] in 'aeiou':
                    count+=1
                else:
                    str2.append(str(count))
                    i+=1
                    break
        else:
            str2.append(str1[i])


s=input().strip()
print(vowelEncryption(s))'''
''' 
eager 
'''


'''def vowelEncryption(str1):
    str2 = ''
    j = 0
    i = 0
    while i in range(len(str1)):
        count = 0
        if str1[i] in 'aeiou':
            for j in range(i, len(str1)):
                if str1[j] in 'aeiou':
                    count += 1
                    if j == len(str1) - 1:
                        str3 = str2 + str(count)
                        str2 = str3
                else:
                    str3 = str2 + str(count) + str1[j]
                    str2 = str3
                    i = j
                    break
        else:
            str3 = str2 + str1[i]
            str2 = str3
        i = i + 1

    print(str2)


s = input().strip()
vowelEncryption(s)'''
'''sentence=input().strip()
vowels='aeiou'
count=0
vowel = False
for letter in sentence:
   if letter in vowels:
       if vowel == False:
           vowel = True
           count = 1
       else:
            count += 1
   else:
        if vowel == True:
            print(count, end="")
            vowel = False
            print(letter, end='')
   print('')
'''
'''sentence=input().strip()
vowels='aeiou'
count=0
vowel = False
for letter in sentence:
    if letter in vowels:
        if vowel == False:
            vowel = True
            count = 1
        else:
            count += 1
    else:
        if vowel == True:
            print(count, end="")
            vowel = False
        print(letter, end='')
print('')'''


'''def vowelEncryption(str):               #eager
    str2 = []
    j = 0
    count = 0
    for i in range(len(str)):      #5
        try:
            if (str2[j] in 'aeiou'):
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        print(flag)
        if str[i] not in 'aeiou':
            if (count != 0):
                str2.append(count)
            str2.append(str[i])
            j += 1
            count = 0
        elif flag == 1:
            # str3=str2[j]+str[i]
            # str2[j]=str3
            count += 1
        else:
            # str2.append(str[i])
            count += 1
        if (i == len(str) - 1):
            if str[i] in 'aeiou':
                if (count != 0):
                    str2.append(count)
    print(str2)


s = input().strip()
vowelEncryption(s)'''
def vowelEncrypt(str1):          #eager
    en_str = []
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    i=0
    while i<len(str1):               #5
        count = 1
        if str1[i] in vowel:
            while i+1<len(str1):
                if str1[i+1] in vowel:
                    count = count+1
                else:
                    en_str.append(str(count))
                    break
                i=i+1
            if i == len(str1)-1 and str1[i-1] in vowel:
                en_str.append(str(count))
        else:
            en_str.append(str1[i])
        i = i+1
    return "".join(en_str)
print(vowelEncrypt("kgooooooooooseee"))