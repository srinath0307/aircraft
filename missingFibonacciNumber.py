'''# Function for nth Fibonacci number
def Fibonacci(n):
	if n<0:
		print("Incorrect input")
	# First Fibonacci number is 0
	elif n==0:
		return 0
	# Second Fibonacci number is 1
	elif n==1:
		return 1
	else:
		return Fibonacci(n-1)+Fibonacci(n-2)'''
'''# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
	print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
	print("Fibonacci sequence upto",nterms,":")
	print(n1)
# generate fibonacci sequence
else:
	print("Fibonacci sequence:")
	while count < nterms:
		print(n1)
		nth = n1 + n2
		# update values
		n1 = n2
		n2 = nth
		count += 1'''
'''
n = int(input())
arr = sorted(map(int, input().split()))
for i in range(2, n):
    if arr[i - 1] + arr[i - 2] != arr[i]:
        print(arr[i] - arr[i - 1])
        quit()
print(arr[-1])'''
N=int(input())
numList=list(map(int,input().split()))
fib=[0,1]
for ctr in range(1,500):
    fib.append(fib[-1]+fib[-2])
print(fib)
minEle,maxEle=min(numList),max(numList)
for num in fib:
    if num>minEle and num<maxEle and num not in numList:
        print(num)
        break
    '''else:
        if num in numList:
            numList.remove(num)'''
else:
    print(maxEle)
''' 
8
0 1 5 8 3 21 1 2
'''