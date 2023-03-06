class Distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def __add__(self, other):
        feetsum=self.feet+other.feet
        inchesum=self.inches+other.inches
        return Distance(feetsum+inchesum//12,inchesum%12)
    def __str__(self):
        return str(self.feet)+" "+str(self.inches)
    def addinches(self,x):
        self.feet=self.feet+(self.inches+x)//12
        self.inches=(self.inches+x)%12
feet,inches=map(int,input().split())
dist1=Distance(feet,inches)
feet,inches=map(int,input().split())
dist2=Distance(feet,inches)
x=int(input())
dist3=dist1+dist2
print(dist3)
dist3.addinches(x)
print(dist3)

