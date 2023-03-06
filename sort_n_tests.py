n=int(input())
mark=[]
for i in range(n):
    mark.append(input().split())
print(mark)
def timesort(time):
    hr,mn=map(int,time.split(":"))
    minutes=hr*60+mn
    return minutes
sortlist=sorted(mark,key=lambda x:(timesort(x[1]),int(x[2]),x[0]))
for i in sortlist:
    print(*i)

"""
5
MathsTest2 10:30 45
PhysicsTest 11:30 75
EnglishTest 10:00 60
MathsTest1 10:30 45
ChemistryTest 10:30 30
6
AptitudeTest 09:30 30 
Maths3Test 10:00 120 
PrinciplesOfManagementTest 09:30 90 
Maths4Test 13:00 150
EnvironmentalScienceTest 09:30 90 
CprogrammingTest 11:45 60
"""
