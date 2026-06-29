from admin import Admin
from stock import Stock
from Product_Menu import Menu
from bill_handling import Hist
from bill import Bill

billing = Bill()

bill_hist=Hist()
m=Menu()

username=input("Username:")
password=input("password:")

ad=Admin()

while not ad.check(username,password):
    print("Wrong Password or username❌❌❌")
    print("Pls enter correct login credentials")
    
    username=input("Username:")
    password=input("password:")
    print("Pls enter correct login credentials")

print("\n"*5)

stk=Stock()

tr=True
while(tr):
    option=input("""
        Choose:
        1. Add Product
        2. Update Product
        3. View Product
        4. Remove Product
        5. Purchase product
        6.Menu
        7.Bill history
        10.Exit
        """)

    if option=='6':
        m.menu()

    elif option=='1':

        U=True
        while U:

            id=int(input("id:"))
            name=input("Name:")
            price=int(input("Price:"))
            quantity=int(input("quantity:"))

            stk.add_product(id,name,price,quantity)
            un=input("want to add more item[y/n]:")

            if  un=='n':
                U=False

    elif option=='2':
        print("Write the things to update")

        id=int(input("id:"))
        name=input("Name:")
        price=int(input("Price:"))
        quantity=int(input("quantity:"))

        stk.update_product(id,name,price,quantity)

    elif option=="3":
        stk.view_product()

    elif option=='4':
        id=int(input("id:"))
        stk.remove_product()

    elif option=='5':
        p=True
        while p:
            id = int(input("id: "))
            quantity = int(input("quantity: "))

            stk.purchase_product(id, quantity)

            purchase_option = input("Add more items? (y/n): ")

            if purchase_option == "n":
                billing.b(stk.product_for_bill)
                stk.product_for_bill.clear()
                p = False

    elif option=='7':
        bill_hist.view_bill_history()

    else:
        print("Have a nice day‼️‼️🤗🤗")
        print("......Exit.....")
        tr=False


        





