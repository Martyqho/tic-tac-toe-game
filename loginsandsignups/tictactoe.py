from flask import Flask, render_template, request redirect, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://localhost:5432/tictactoe"
app.secret_key = "jgfhdje78f9e78r9r789edfjlhwrjllk"
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(
    db.String(10000),
    primary key = True
    )
