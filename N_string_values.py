'''N = int(input())
lines = []
def divider(S):
    div = []
    for ctr in range(0,len(S),len(S)//4):
        div.append(S[ctr:ctr+len(S)//4])
    return div
for ctr in range(N):
    lines.append(divider(input()))
print(lines)
print(N//2)
for row in range(0,N,2):              #4
    for col in range(0,len(lines[0])):
        print(lines[row][col]+lines[row+1][col])'''
# 00|10
# 01|11
'''
4
PondLionNoteBook
MarkBoysHeadBird
crowdogseggscake
roadmapsjunesilk

6
abcdefghijkl
ABCDEFGHIJKL
MNOPQRSTUVWX
mnopqrstuvwx
123456789012
AaBbCcDdEeFf
'''
n=int(input())

def divider(s):
    word = []
    for i in range(0,len(s),len(s)//4):
        word.append(s[i:i+len(s)//4])
    return word
words=[]
for i in range(n):
    words.append(divider(input().strip()))
for row in range(0,n,2):
    for col in range(0,n//2):
        print(words[row][col]+words[row+1][col])
