from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import city

@app.route("/users/new")
def home():
    return render_template("home.html")

@app.route("/users/show")
def show():
    return render_template("show.html" , all_users = city.City.return_users())


@app.route("/users/add_to_db", methods=["POST"])
def add_city_to_db():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    city.City.create_user(data)
    return redirect("/users/show")