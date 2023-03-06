'''import datetime as datetime
d=datetime.datetime(2018,2,3)

date_object = datetime.datetime.strftime(d, "%d-%m-%Y")
print("date_object =", date_object)'''
#thunderCodes;
'''from datetime import datetime
N = int(input())
dates = []
for ctr in range(1,N+1):
    #print(input())
    dateCurr = datetime.strptime(input().strip(),"%d-%b-%Y")
    dates.append(dateCurr)
print(dates)
dates = sorted(dates,key = lambda date : [date.day,date.month,date.year])
print(dates)
for date in dates:
    print(date.month)
    print(date.__format__("%d-%b-%Y"))'''

''' 
10
31-Jan-1990    # ['31','Jan','1990']
15-Jul-2021
15-Feb-2011
15-Sep-2009
08-Aug-2019
01-Dec-2050
15-Jul-2019
15-Jul-2010
07-Mar-2019 
29-Feb-2000 
'''

n=int(input())
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dates=[]
for i in range(n):
    date=input().strip().split('-')
    dates.append(date)
dates=sorted(dates,key=lambda x:(int(x[-1]),months.index(x[1]),int(x[0])))
for i in dates:
    print(*i,sep='-')

'''n=int(input())
li1=list(map(int,input().split()))
li2=list(map(int,input().split()))
for i in range(n):
    comp=li1[i]
    length=li2[i]
    sub=[];ctr=0
    #print(comp,length)
    for j in range(i,n):
        if li1[j]>=comp:
            ctr+=1
            sub.append(li1[j])
        else:
            sub.append(li1[j])
        if ctr==length:
            break
    #print(ctr,sub)
    if ctr!=length:
        print(-1,end=' ')
    else:
        print(len(sub),end=' ')'''
''' 
5
9 2 5 2 10
2 3 6 1 1 
'''