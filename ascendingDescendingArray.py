n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
if len(set(arr1))==1 and len(set(arr2))==1:
    if arr2[0]<arr1[0]:
        print(*arr2)
        print(*arr1)
    else:
        print(*arr1)
        print(*arr2)
elif sorted(arr1)[::-1]==arr1 and len(set(arr2))==1:
    print(*arr2)
    print(*arr1)
elif sorted(arr2)[::-1]==arr2 and len(set(arr1))==1:
    print(*arr1)
    print(*arr2)
elif len(set(arr1))==1:
    print(*arr2)
    print(*arr1)
elif len(set(arr2))==1:
    print(*arr1)
    print(*arr2)
elif sorted(arr1)==arr1:
    print(*arr1)
    print(*arr2)
else:
    print(*arr2)
    print(*arr1)
''' 
4
10 10 9 5
5
10 10 15 25 80
'''
''' 
5
15 15 15 15 15
4 
10 10 10 10
'''
''' 
5
15 15 15 15 15
4
15 15 15 15
'''
''' 
4
15 15 15 15
5 
15 15 15 15 15 
'''
