'''a0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
a1=range(10)
a2=sorted([i for i in a1 if i in a0])
a3=sorted([a0[s] for s in a0])
a4=[i for i in a1 if i in a3]
#a5={[i:i*i for i in a1]}
a6=[[i,i*i] for i in a1]
print(a0,a1,a2,a3,a4,a6)'''

'''l1=[int(val) for val in input().split()]
l2=[int(val) for val in input().split()]
i=0
j=len(l2)-1
while i<len(l1):
    print(l1[i],l2[j])
    i+=1
    j-=1'''
'''
li=['a','b','c']
tup=tuple(li)
print(li,tup)
tup=('a','b','c')
lii=list(tup)
print(tup,lii)'''
'''arr=[int(val) for val in input().split()]
i=1
count=0
print(arr)
while i<len(arr):
    if arr[i]%2!=0:
        count+=1
    i+=2
print(count)'''



'''
from checkBalance import check_balance
accountNumber=input()
print(check_balance(accountNumber))



# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def check_balance(self,accountNumber):
		print("\n Net Available Balance=",self.balance)

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()









def check_balance(accountNumber):

if __name__ == '__main__':
'''
'''li=[val for val in range(1, 101)]
finlist=[]
for i in li:
    if i%2==0 and i%4==0 and i%5==0:
        finlist.append(i)
oddcount=0
evencount=0
for i in finlist:
    if i%2==0:
        evencount+=1    #1
    else:
        oddcount+=1
print("evencount:",evencount,"oddcount:",oddcount)
print("slicing from 1-20", finlist[1:21])
print("slicing from 21-50", finlist[21:51])    #2
print("slicing from 51-100", finlist[51:101])
n=int(input())
if n in finlist:
    print("present")
else:
    print("not present")'''









'''M=int(input())
powerbanksC=list(map(int,input().split()))
N=int(input())
phonesC=sorted(list(map(int,input().split())),reverse=True)                #99 85 50 0
count=0;totalCharge=sum(powerbanksC)
for charge in phonesC:
    requiredCharge=100-charge
    if totalCharge-requiredCharge>=0:
        count+=1
        totalCharge-=requiredCharge
    else:
        break
print(count)'''

''' 
2
51 25                        totalCharge=76    75    60   10     
4
0 99 50 85
'''
''' 
2
50 100 
5
20 30 40 50 20 
'''


















