'''class RegistrationNumberGenerator:
    def __init__(self,li):
        self.li=li
    def sorting(self):
        dict={}
        for i in self.li:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        indec=1
        for j in dict.keys():
            for k in li:
                if k==j:
                    index=li.index(k)
                    self.li[index]+=(" 00{}".format(indec))
                    indec+=1
            indec=1
    def remove(self,string):
        return string.replace(" ", "")
n=int(input())
li=[]
for i in range(n):
    li.append(input())
obj=RegistrationNumberGenerator(li)
obj.sorting()
for i in li:
    print(obj.remove(i))'''

"""
9
2021 A
2021 A
2021 B
2021 A
2020 C
2020 C
2020 A
2020 C
2020 C
"""
"""
15
2018 E
2018 E
2018 E
2018 E
2018 E
2018 E
2020 A
2020 B
2020 C
2020 D
2020 E
2019 C
2019 C
2019 A
2019 A
"""