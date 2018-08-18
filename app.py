from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/<user>")
def index(user = None):
    return render_template("user.html",user=user)


@app.route("/shopping")
def shopping():
    foods = ["Chinese", "Tuna", "Beef"]
    return render_template("shopping.html", foods=foods)

@app.route("/login_page")
def login_page():
    return render_template("login_page.html")


@app.route("/login_verification", methods=['GET', 'POST'])
def login_verification():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        login_info = dict();
        login_info = {"username": username, "password": password}
        return render_template("user_panel.html", login_info=login_info)
    return render_template("user.html")


if __name__ == '__main__':
    app.run()
