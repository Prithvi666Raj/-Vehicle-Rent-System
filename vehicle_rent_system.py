class VehicalShop:

    def __init__(self,stock):
        self.stock=stock
    def display_vehical(self):
        print("Total Vehical",self.stock)
    def ren_for_vehical(self,p):

        if p<=0:
            print("Enter the valid number :- ")
        elif p>self.stock:
            print("Enter The Number Of Vahical you want :- ")
        else:
            self.stock=self.stock-p
            print("Total price",p*100)
            print("Total Vehical Currently in Stock :- ",self.stock)
while True:
    obj = VehicalShop(1820)
    b=int(input('''
    1 Display Stock
    2 Rent a Vehical
    3 Exit
    ''')) 
    if b==1:
        obj.display_vehical()
    elif b==2:
        n=int(input("Enter the Quentity :- "))
        obj.ren_for_vehical(n)
    else:
        break           
