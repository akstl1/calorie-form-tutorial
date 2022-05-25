from flask import Blueprint, render_template

views = Blueprint('views',__name__)

# creates home route, defines the function to run when the route is called
@views.route('/')
def home():
    return render_template("home.html")
