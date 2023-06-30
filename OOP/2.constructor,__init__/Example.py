class item:
    pay_rate = 0.8  # after 20% discount
    all=[]
    def __init__(self,name,price,quantity=0):

        assert price >=0 ,f"price {price} is not greater than or equal to 0!!!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to 0!!!"

        self.name=name
        self.price=price
        self.quantity=quantity

        #action to execute
        item.all.append(self)

    def total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate

    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})\n"

item1=item("car",100,10)
item2=item("bike",200,20)
item3=item("mobile",3000,30)
item4=item("shops",400,40)
item5=item("food",500,50)

print(item.all)
