import os

import simplejson

from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.user_name

@app.route('/')
def home():
    return simplejson.dumps([ dict(id = u.id,
                                   user_name = u.user_name,
                                   email = u.email) for u in User.query.all()])

if __name__ == '__main__':
    app.run()

