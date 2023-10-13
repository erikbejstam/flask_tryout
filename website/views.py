from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/') #när man går till route / så kommer den funk köras
def home():
    return render_template("home.html")









