import csv


class item:
    pay_rate = 0.8  # after 20% discount
    all=[]
    def __init__(self,name,price,quantity=0):

        assert price >=0 ,f"price {price} is not greater than or equal to 0!!!"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to 0!!!"

        self.name=name
        self.price=price
        self.quantity=quantity

        item.all.append(self)

    def total(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)

        for Item in items:
            item(
                name=Item.get('name'),
                price=float(Item.get('price')),
                quantity=int(Item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        #count float that are decimal
        #ex 5.0 , 10.0
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"item('{self.name}',{self.price},{self.quantity})\n"

print(item.is_integer(9.25))
# item.instantiate_from_csv()
# print(item.all)

