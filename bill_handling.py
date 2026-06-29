from datetime import datetime

class Hist:

    def __init__(self):
        pass

    def generate_bill(self, products):

        total = 0

        

        with open("bill_history.txt", "a") as file:

            file.write("\n")
            file.write("=" * 50 + "\n")
            file.write(f"Date : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            file.write("-" * 50 + "\n")
            file.write("ID\tName\tPrice\tQty\tAmount\n")

            for product in products:

                amount = product["price"] * product["quantity"]
                total += amount

                

                file.write(
                    f'{product["id"]}\t'
                    f'{product["name"]}\t'
                    f'{product["price"]}\t'
                    f'{product["quantity"]}\t'
                    f'{amount}\n'
                )

           

            file.write("-" * 50 + "\n")
            file.write(f"Total = {total}\n")
            file.write("=" * 50 + "\n")

    def view_bill_history(self):

        try:
            with open("bill_history.txt", "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("No bill history found.")