from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Item(db.Model):
    idNum = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)


@app.route("/hello")
@app.route("/hello/")
@app.route("/hello/<user_name>")
def hello(user_name=None):
    return render_template('home.html', user=user_name)