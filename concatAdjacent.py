'''n=int(input())
li=input().split()
val=int(input())
flag=False
for i in range(0,len(li)-1):
    if int(li[i]+li[i+1])%val==0:
        print(li[i],li[i+1])
        flag=True
    elif int(li[i+1]+li[i])%val==0:
        print(li[i+1],li[i])
        flag=True
if not flag:
    print("-1")'''
""" 
6
2 4 8 6 5 11
4
"""
'''while True:
    try:
        n=input().split()
        summ=0
        for i in n:
            if i.isdigit():
                summ+=int(i)
            else:
                break
        print(summ)
    except:
        break'''