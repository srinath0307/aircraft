strs = ["flower","flow","flight"]
def longestCommonPrefix(S):
    if (len(S) == 0):
        return ""
    for i in range(len(S[0])):#6
        c = S[0][i] #f
        for j in range(len(S)): #3
            if (i == len(S[j]) or S[j][i] != c):
                return S[0][0:i];
    return S[0]


s=strs[0];ctr=0;flag=1
while flag==1:
        for i in strs:
            if s[:ctr]==i[:ctr]:
                flag=1
                print(s[:ctr],i[:ctr])
            else:
                flag=0
                print("entered")
                break
        ctr+=1
        print(ctr)