from flask import Flask, render_template, request, redirect, url_for, flash, session
from admin import Admin
from stock import Stock
from bill_handling import Hist

his=Hist()

app = Flask(__name__)

# stored credentials
admin = Admin()
stock = Stock()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if admin.check(username, password):
        return render_template("dashboard.html")
    else:
        return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add-product", methods=["GET", "POST"])
def add_product():

    if request.method == "POST":

        id = int(request.form["id"])
        name = request.form["name"]
        price = int(request.form["price"])
        quantity = int(request.form["quantity"])

        stock.add_product(id, name, price, quantity)

        return redirect(url_for("dashboard"))

    return render_template("add_product.html")



@app.route("/view_product", methods=["GET", "POST"])
def view():

    if request.method == "POST":
        action = request.form.get("action")

        if action == "back":
            return redirect(url_for("dashboard"))

    products = stock.view_product()

    return render_template(
        "view_product.html",
        products=products
    )

# @app.route("/purchase", methods=["GET", "POST"])
# def purchase():
#     if request.method == "POST":
#         action = request.form.get("action")

#         product_id = request.form.get("id")
#         quantity = request.form.get("quantity")

#         if action == "add_more":
#             # save item or update cart logic
#             return redirect(url_for("purchase"))

#         elif action == "bill":
#             return redirect(url_for("bill"))

#     return render_template("purchase.html")

@app.route("/purchase", methods=["POST", "GET"])
def purchase():

    if request.method == "POST":

        action = request.form.get("action")

        item = {
            "id": int(request.form.get("id")),
            "name": "Demo Product",
            "price": 100,
            "quantity": int(request.form.get("quantity"))
        }

        stock.add_to_bill(item)

        if action == "bill":
            return redirect(url_for("bill"))
        else:
            return redirect(url_for("purchase"))

    return render_template("purchase.html")


@app.route("/bill")
def bill():

    bill_items = stock.product_for_bill

    his.generate_bill(bill_items)

    total = 0
    for item in bill_items:
        total += item["price"] * item["quantity"]

    return render_template("bill.html",
                           bill_items=bill_items,
                           total=total)


@app.route("/bill_history")
def bill_history():

    try:
        with open("bill_history.txt", "r") as file:
            history = file.read()

    except FileNotFoundError:
        history = "No bill history found."

    return render_template("bill_history.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)