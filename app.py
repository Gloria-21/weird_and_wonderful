import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# Database app
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # check if username already exists
        if mongo.db.users.find_one(
                {"username": request.form.get("username").lower()}):
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(register)

        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # check that the user has been successfully registerd
        print('registered_user: ')
        print(registered_user)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user[
                    "password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                        request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # take the session user's username from de db
    username: mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_lot", methods=["GET", "POST"])
def add_lot():
    # allows user to create a lot
    if request.method == "POST":
        lot = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name").lower(),
            "description": request.form.get("description").lower(),
            "estimate_price": request.form.get("estimate_price"),
            "created_by": session["user"]
        }
        mongo.db.lots.insert_one(lot)
        flash("Your lot has been successfully added")
        return redirect(url_for("profile", username=session['user']))

    return render_template("add_lot.html")

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_lot.html", categories=categories)


@app.route("/edit_lot/<name_id>", methods=["GET", "POST"])
def edit_lot(name_id):
    # allows user to edit a lot
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name").lower(),
            "description": request.form.get("description").lower(),
            "estimate_price": request.form.get("estimate_price"),
            "created_by": session["user"]
        }
        mongo.db.lots.update({"_id": ObjectId(name_id)}, submit)
        flash("Lot sucessfully updated")

    name = mongo.db.find_one({"_id": ObjectId(name_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_lot.html", name=name, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
