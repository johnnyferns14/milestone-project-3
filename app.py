from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Home Page")


@app.route('/customer-login')
def customer_login():
    return render_template("customer-login.html", title="Login Page")


@app.route('/customer-registration')
def customer_registration():
    return render_template("customer-registration.html", title="Sign Up")


@app.route('/seller-registration')
def seller_registration():
    return render_template("seller-registration.html", title="Sign Up")


@app.route('/seller-login')
def seller_login():
    return render_template("seller-login.html", title="Login")


@app.route('/seller-dashboard')
def seller_dashboard():
    return render_template("seller-dashboard.html", title="Seller Dashboard")


if __name__ == "__main__":
    app.run(debug=True)
