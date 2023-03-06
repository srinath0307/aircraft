s=input().strip()
letters=''
mid=len(s)//2
ctr=1
letters+=s[mid]
while ctr<len(s):
    if (mid+ctr)==len(s) or (mid-ctr)==-1:
        print(mid-ctr)
        print(mid+ctr)
        print("if 1 executed")
        break
    if s[mid-ctr] in letters:
        print("second if executed ")
        letters+=s[mid-ctr]
        break
    else:
        letters+=s[mid-ctr]
    if s[mid+ctr] in letters:
        print("third if executed")
        letters+=s[mid+ctr]
        break
    else:
        letters+=s[mid+ctr]
    ctr+=1
print(letters)