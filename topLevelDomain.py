s = input().strip()
s = s.split('//')
print(s)
s = ''.join(s[1:])
s = s.split('/')
k = s[0][::-1].index('.')
k = len(s[0]) - k
print(s[0][k - 1:])


'''
https://www.skillrack.com/solve/8464
'''