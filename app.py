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
    dict_for_pass = {"id":obj.id,"name":obj.name,"description":obj.description,"createdBy":obj.createdBy,"topic":obj.topic,"blogBody":obj.blogBody,"isPosted":obj.isPosted}
    data_for_validation = blog_method(dict_for_pass)
    insert = datetime.now()
    dict_for_pass["createdAt"] = insert.strftime("%d/%m/%Y %H:%M:%S")
    dict_for_pass["postedAt"] = insert.strftime("%d/%m/%Y %H:%M:%S")
    dict_for_pass["blogSize"] = len(dict_for_pass['blogBody'].split(" "))
    return jsonify(insert_data(dict_for_pass))


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