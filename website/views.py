from flask import Blueprint

views = Blueprint('views',__name__)

# creates home route, defines the function to run when the route is called
@views.route('/')
def home():
    return "<h1>Test</h1>"
