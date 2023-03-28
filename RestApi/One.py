from flask import Flask
from flask_restful import Api,Resource
app=Flask(__name__)
api=Api(app)
class hello_world(Resource):
    def get(self):
        return {"name":"hello"}
    
# Add class to resource
api.add_resource(hello_world,'/hello')
if __name__=='main':
    app.run(debug=True)
    