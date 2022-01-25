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
def index():
    tasks = mongo.db.index.find()
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
        
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        print('existing_user: ')
        print(existing_user)            

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email")
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
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
