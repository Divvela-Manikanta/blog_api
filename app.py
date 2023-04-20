from flask import Flask,request,jsonify
from dataclasses_Scripts import blog_valid
from validation import blog_method
from datetime import datetime
from MongoOperation import *


app = Flask(__name__)


@app.route("/createblog",methods=["POST"])
def create_blog():
    data = request.get_json()
    obj = blog_valid.from_dict(data) 
    data_for_validation = blog_method(obj)
    insert = datetime.now()
    data_for_validation["createdAt"] = insert.strftime("%d/%m/%Y %H:%M:%S")
    data_for_validation["postedAt"] = insert.strftime("%d/%m/%Y %H:%M:%S")
    data_for_validation["blogSize"] = len(data_for_validation['blogBody'].split(" "))
    return jsonify(insert_data(data_for_validation))


@app.route("/dashboard",methods=["POST"])
def user_dashboard():
     data = dict(request.get_json())
     return jsonify(user_blog(data))
    

@app.route("/<blogid>")
def blog(blogid):
    return jsonify(blog_info(blogid))

@app.route("/overall",methods=["POST","GET"])
def over_all():
     if request.method =="POST":
        data = request.get_json()
        return jsonify(total_blog(data))
     if request.method =="GET":
            data = {}
            data['page'] = 0
            data['pageSize'] =9
            return jsonify(total_blog(data))
   

@app.route("/delete",methods=["POST"])
def delete_post():
      data = dict(request.get_json())
      return jsonify(delete_data(data))
    
@app.route("/update",methods=["POST"])
def update():
     data = dict(request.get_json())
     return jsonify(update_the_data(data))


if __name__ == "__main__":
    app.run(debug=True)