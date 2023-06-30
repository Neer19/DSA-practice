class item:
    pay_rate = 0.8  # after 20% discount
    def __init__(self,name,price,quantity=0):

        # print(f"Assigned value={name}")

        #run validation to the received argument
        # assert  is a keword that is used to check if there is a match between what is happening to your expectations.
        assert price >=0 ,f"price {price} is not greater than or equal to 0!!!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to 0!!!"


        #assign to self object
        self.name=name    #dynamically assigned the value
        self.price=price
        self.quantity=quantity

    def total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate

item1=item("Food",500,2)
item1.apply_discount()
print(item1.price)
# if we pass "500" parameter then it will print 500 2 times because we take the quantity 2.

# item1.name="Food"
# item1.price=500
# item1.quantity=2
# print(item1.total(item1.price,item1.quantity))

item2=item("Books",5000,3)
item2.pay_rate=0.4
item2.apply_discount()
print(item2.price)
# item2.name="Books"
# item2.price=5000
# item2.quantity=3
# print(item2.total(item2.price,item2.quantity))

# print(item1.total())
# print(item2.total())
# print(item1.name)
# print(item2.name)
# print(item1.price)
# print(item2.price)
# print(item1.quantity)
# print(item2.quantity)

# print(item.__dict__) #All the attribute for class level
# print(item1.__dict__) #All the attribute for instance level

