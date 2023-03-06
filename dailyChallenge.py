'''n=int(input())
l=list(map(int,input().split()))
summ=0
for i in range(n):
    val=str(len(str(l[i])))+str(l[i])
    print(val)
    summ+=int(val)
print(summ)'''
n,m=map(int,input().split())
def binarySearch(arr,start,end,ele):
    while start<=end:
        mid=start+(end-start)//2
        if arr[mid]==ele:
            return 1
        elif arr[mid]<ele:
            start=mid+1
        else:
            end=mid-1
    return 0
l1=sorted(list(map(int,input().split())))
k=sorted(list(map(int,input().split())))
ctr=0
for i in k:
    if binarySearch(l1,0,len(l1)-1,i):
        ctr+=1
print(ctr)