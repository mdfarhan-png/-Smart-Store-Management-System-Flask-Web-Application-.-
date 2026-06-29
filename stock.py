# Store

#    ├── add_product()
#    ├── remove_product()
#    ├── update_product()
#    ├── purchase_product()
#    └── view_products()

# {
#         "id": 101,
#         "name": "Keyboard",
#         "price": 799,
#         "quantity": 20
#     }


import pandas as pd
from bill import Bill


billing=Bill()
class Stock:

    def __init__(self):
        
        
        self.products = []
        self.product_for_bill = []

    def add_to_bill(self, item):
        self.product_for_bill.append(item)


    def update_product(self,id,name=None,price=None,quantity=None):
        for product in self.products:
            if product["id"]==id:
                if name is not None:
                    product["name"]=name
                if price is not None:
                    product["price"]=price
                if quantity is not None:
                    product["quantity"]=quantity
        print("Stock updated successfully🤗🤗")
                
        

    def add_product(self,id,name,price,quantity):
       
            product={
                "id":id,
                "name":name,
                "price":price,
                "quantity":quantity
            }

            self.products.append(product)
            print("Product added successfully 💯💯‼")
            
        

    def purchase_product(self, id, quantity):

        for product in self.products:
            if product["id"] == id:

                if product["quantity"] < quantity:
                    print("Insufficient stock")
                    return

                prod = {
                    "id": product["id"],
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": quantity
                }

                self.product_for_bill.append(prod)

                product["quantity"] -= quantity

                
                return

        print("Please check the product ID again.")


    def view_product(self):
        return self.products

    def remove_product(self,id):
        p=[]
        for product in self. products:
            if product["id"]!=id:
                p.append(product)
        products=p 



    
          