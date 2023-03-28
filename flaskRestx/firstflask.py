from flask import Flask,jsonify,request
from flask_restx import Api,Resource,fields
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
import json
import os
from datetime import datetime
app=Flask(__name__)
api=Api(app)
CORS(app)

# basedir=os.path.dirname(os.path.realpath(__file__))
# print(basedir+"file name")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/pythontest' 
# app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_ECHO']=True
db=SQLAlchemy(app)

# Done for creating Table==========
class Book(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    title=db.Column(db.String(90),nullable=False)
    author=db.Column(db.String(89),nullable=False)
    date_added=db.Column(db.DateTime(),default=datetime.utcnow)
    def __rep__(self):
        return self.title


book_model=api.model('Book',
    {
        'id':fields.Integer(),
        'title':fields.String(),
        'author':fields.String(),
        'date_added':fields.DateTime(),

    }
)

@api.route('/books')
class Books(Resource):
    @api.marshal_list_with(book_model,code=200,envelope="books")
    def get(self):
        books=Book.query.all()
        print("books***********")
        print(books)
        return books
        # return jsonify({"message":"hello suhel from get"})
    @api.marshal_list_with(book_model,code=200,envelope="books")
    def post(self):
       data= request.get_json();
       title=data.get('title')
       author=data.get('author')
       book=Book(title=title,author=author)
       db.session.add(book)
       db.session.commit()
       books=Book.query.all()
       return books



@api.route('/book/<int:id>')
class BookResource(Resource):
    @api.marshal_with(book_model,code=201 ,envelope="book ")
    def get(self,id):
        book=Book.query.get_or_404(id)
        return book
    @api.marshal_with(book_model,code=201 ,envelope="book ")
    def put(self,id):
        book_data=request.get_json();
        book=Book.query.get_or_404(id)
        book.author=book_data.get('author'),
        book.title=book_data.get('title');
        db.session.add(book)
        db.session.commit()
        books=Book.query.all()
        return books
    @api.marshal_with(book_model,code=201 ,envelope="book ")
    def delete(self,id):
        book_delete=Book.query.get_or_404(id)
        db.session.delete(book_delete)
        db.session.commit()
        return "Deleted Successfully"

# @app.shell_context_processor
# def make_shell_context():
#     return {
#         'db':db,
#         'Book':Book
#     }

if __name__=='__main__':
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
    
    