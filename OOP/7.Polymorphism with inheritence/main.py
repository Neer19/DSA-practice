class veh:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def get_detail(self):
        print("name=",self.name)
        print("color=",self.color)
        print("price=",self.price)

    def max_speed(self):
        print("max speed is 360")

    def gear(self):
        print("gear change is 5")


class car(veh):
    def max_speed(self):
        print("max speed is 120")

    def gear(self):
        print("gear change is 4")

v1=veh("truck","blue",4500000)
c1=car("car","gray",1200000)

v1.max_speed()
c1.max_speed()