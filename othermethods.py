from flask import Flask,jsonify,request


app = Flask(__name__)

students_list = {"user1":1,
                 "user2":2,
                 "user3":3,
                 "user4":4}


@app.route("/getdata",methods=["get"])
def getdata():
    return jsonify(students_list)


@app.route("/putdata",methods=["POST"])
def putdata():
    data = request.get_json()
    students_list.update(data)
    return jsonify(students_list)

@app.route("/delete/<id>",methods=["delete"])
def delete(id):
    del students_list[id]
    return jsonify(students_list)

@app.route("/update",methods=["put"])
def uupdate():
    data = dict(request.get_json())
    for val in data.keys():
        students_list[val] = data[val]
    return jsonify(students_list)


if __name__ =="__main__":
    app.run(debug= True,port=9999)