class bikeShope(object):
    def __init__(self, stock):
        self.stock=stock
    def displayBike(self):
       print("Toatl Bike",self.stock)
       
    def rentForBike(self,q):
        if q <= 0:
            print("Enetr the positive value or greater then zero")
        if q > self.stock:
            print("Enter the value ( less than stock)")
        else:
            self.stock=self.stock
            print("Total prise",q*100)
            print("Total Bikes",self.stock)
            
while True:
    obj=bikeShope(100)
    uc=int(input('''
1 Display stocks
2 Rent a Bike
3 Exit
                 
                 
                 
                 '''))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the Qty:--"))
        obj.rentForBike(n)
    else:
        break
        