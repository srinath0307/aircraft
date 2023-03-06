'''class ElectricityBill:
    def __init__(self,consumerNo,consumerName):
        self.consumerNo = consumerNo
        self.consumerName = consumerName
    def currentbill(self,previousMonthReading,currentMonthReading,type):
        unit=previousMonthReading-currentMonthReading
        self.summ=0
        if type=='domestic':
            if unit<=100:
                self.summ+=unit
            elif unit>100 and unit<=200:
                self.summ+=100
                unit-=100
                for i in range(1,unit+1):
                    self.summ+=2.50
            elif unit>200 and unit<=500:
                self.summ+=100
                self.summ+=250
                unit-=200
                for i in range(1,unit+1):
                    self.summ+=4
            elif unit>500:
                self.summ += 100
                self.summ += 250
                self.summ+=1200
                unit -=500
                for i in range(1,unit+1):
                    self.summ+=6
        elif type=='commercial':
            if unit<=100:
                for i in range(1,unit+1):
                    self.summ+=2
            elif unit>100 and unit<=200:
                self.summ+=200
                unit-=100
                for i in range(1,unit+1):
                    self.summ+=4.50
            elif unit>200 and unit<=500:
                self.summ+=200
                self.summ+=450
                unit-=200
                for i in range(1,unit+1):
                    self.summ+=6
            elif unit>500:
                self.summ += 200
                self.summ += 450
                self.summ+=1800
                unit -=500
                for i in range(1,unit+1):
                    self.summ+=7
        return self.summ

obj=ElectricityBill(1234,"srinath")
print(obj.currentbill(400,200,"domestic"))
'''
'''n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=i:
        print(i,end = " ")
        j = j+1
    i = i+1
    print()'''
