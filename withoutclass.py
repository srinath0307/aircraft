class electricity_bill:
    def __init__(self,current_month,previous_month,customer_name,Type):
        self.totalCurrentConsumed = current_month - previous_month
        self.name = customer_name
        self.Type = Type
        self.totalCharge = 0
    def get_total_bill(self):
        if self.Type == "c":
            if(self.totalCurrentConsumed <= 100):
                self.totalCharge = self.totalCurrentConsumed*2
            elif(self.totalCurrentConsumed in range(101,201)):
                self.totalCharge = 100*2+(self.totalCurrentConsumed-100)*4.5
            elif(self.totalCurrentConsumed in range(201,501)):
                self.totalCharge = 100*2+100*4.5+(self.totalCurrentConsumed-200)*6
            else:
                self.totalCharge = 100*2+100*4.5+300*6+(self.totalCurrentConsumed-500)*7
        if self.Type == "d":
            if(self.totalCurrentConsumed <= 100):
                self.totalCharge = self.totalCurrentConsumed*1
            elif(self.totalCurrentConsumed in range(101,201)):
                self.totalCharge = 100*1+(self.totalCurrentConsumed-100)*2.5
            elif(self.totalCurrentConsumed in range(201,501)):
                self.totalCharge = 100*1+100*2.5+(self.totalCurrentConsumed-200)*4
            else:
                self.totalCharge = 100*1+100*2.5+300*4+(self.totalCurrentConsumed-500)*6
    def __str__(self):
        return "{} is your electricity bill".format(self.totalCharge)
name = input("customer Name ? : \n")
prevUsage = int(input("previous_month Usage ? : \n"))
currUsage = int(input("currentMonth Usage ? : \n"))
print("d - domestic power\nc - commercial power")
Type = input()
bill = electricity_bill(currUsage,prevUsage,name,type)
bill.get_total_bill()
print(bill)