# from flask import Flask, render_template, request

# app = Flask(__name__)

class Admin:

    def __init__(self):
        # Define your actual credentials here as strings
        self.username = "Farhan"
        self.password = "123456"

    def check(self, name, pas):
        return name == self.username and pas == self.password
        # if(name == self.username and pas == self.password):
        #     print("Login Successfully")

        # else:
        #     print("Username or password is wrong")


# admin = Admin("far", "123")


# @app.route("/")
# def home():
#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def login():

#     username = request.form["username"]
#     password = request.form["password"]

#     if admin.check(username, password):
#         return "Login Successful"

#     return "Invalid Username or Password"


# if __name__ == "__main__":
#     app.run(debug=True)