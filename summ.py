r,c=map(int,input().split())
cities=[]
# For user input
for i in range(r):          # A for loop for row entries
    a =[]
    for j in range(c):      # A for loop for column entries
         a.append(int(input()))
    cities.append(a)
signal=[[['0']*c for row in range(r)]]
signalRecieved=0
for row in range(0,r):
    for col in range(0,c):
        if cities[row][col]=='L':
            for srow in range(max(0,row-2),min(r,row+3)):
                for scol in range(max(0,col-2),min(c,col+3)):
                    signal[srow][scol]='#'
        elif cities[row][col]=='S':
            for srow in range(max(0,row-1),min(r,row+2)):
                for scol in range(max(0,col-1),min(c,col+2)):
                    signal[srow][scol]='#'
for row in signal:
    signalRecieved+=row.count('#')
print(signalRecieved)
'''0 0 0 0 0 0 0 0
0 S 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 S 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 L 0 0
0 0 0 0 0 0 0 0
S 0 0 0 0 0 0 0'''
