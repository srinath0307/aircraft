n=int(input())
l=[]
d={}
for i in range(n):
	a=input().strip()
	d[a]=d.get(a,0)+1
	print(a,end="")
	if d[a]>1:
		print(d[a],end=" ")
	print()


'''d={}
for i in l:
	if i not in d:
		d[i]=1
	else:
		d[i]+=1
print(d)
c=0
print(len(d))
while c<=len(d):
	for i in d.keys():
		if d[i]<=1:
			print(d.keys()[c])
		else:
			print("{}{}".format(d.keys()[c],d[i]))
		c+=1'''
"""10'''
following
memento
insomnia
inception
interstellar
memento 
dark
inception
interstellar
inception"""