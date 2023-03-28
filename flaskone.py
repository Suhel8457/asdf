from flask import Flask,render_template,current_app,jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug=True
# adding configuration for using a sqlite database
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)


class Item(db.Model):
   # Creating a Column with size of 30 char
   name=db.Column(db.String(length=30),nullable=False)
   price=db.Column(db.Integer(),nullable=False)
   barcode=db.Column(db.String(length=12),nullable=False)
   description=db.Column(db.String(length=1024),nullable=False)
   #Creting a identifier which is the Primary Key
   id=db.Column(db.Integer(),primary_key=True)
   def __repr__(self) :
      return f'{self.name} {self.price}'

@app.route('/')
def hello_world():
   #data=[{'name':"suhel"},{'name':"kiskore"}]
   data=Item.query.all()
   print(data)
   return render_template('Home.html',name=data)
# @app.route('/gadgets')
# def list_of_books():
#     books = [
#         {'name': 'The Call of the Wild', 'author': 'Jack London'},
#         {'name': 'Heart of Darkness', 'author': 'Joseph Conrad'}
#     ]
#     return json.dumps({"name":'suhel'},{"name":"vamsi"})
@app.route('/suhel', methods=['GET'])
def home():
    return "Welxome"

@app.route('/home')
def check():

   return render_template('Base.html')

if __name__ == "__main__":
   #  db.create_all()
    app.run(debug=True)