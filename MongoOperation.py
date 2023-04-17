from pymongo import MongoClient 
from datetime import datetime


conn = MongoClient("localhost",27017)
db = conn.blog
collection = db.blogcoll


def insert_data(data):
    try:
        check = collection.find_one({"id":data['id']})
        if check == None:
            validate = collection.insert_one(data)
            return ({"Meassage":"Data is inserted successfully.",
                        "Success": True,
                        "Status":200})
        else:
            return ({"Meassage":"Blogid is already exist.please try with  diffrent blogid.",
                        "Success": True,
                        "Status":200})

    except Exception as ex:
        return ({"Meassage":"something went wrong try again.",
                      "Success": False,
                      "Status":200})

def user_blog(data):
    output = collection.aggregate([
        {"$match":{"createdBy":data['createdBy']}},
        {"$sort":{"createdAt":-1}},
        {"$project":{"_id":0}} ]) 
    list_trans=[]
    for val in output:
        list_trans.append(val)
    if(len(list_trans)!=0):
        return ( list_trans)
    else:
        return ({"Meassage":"No data to display.",
                      "Success": True,
                      "Status":200})
    

def blog_info(id):
    out = collection.find_one({"id":id},{"_id":0,"id":0})
    if out !=None:
        return out
    else:
        return ({"Meassage":"No data to display.",
                      "Success": True,
                      "Status":200})
    

    

def total_blog(data):
    output = collection.aggregate([
        {"$match":{"isPosted":"yes"}},
        {"$sort":{"createdAt":-1}},
        {"$skip":data['page']},
        {"$limit":data['pageSize']},
        {"$project":{"_id":0,"name":1,"description":1,"createdBy":1,"postedAt":1}} ]) 
    list_trans=[]
    for val in output:
        list_trans.append(val)
    if(len(list_trans)!=0):
        return ( list_trans)
    else:
        return ({"Meassage":"No data to display.",
                      "Success": True,
                      "Status":200})
    
def delete_data(data):
    out = collection.find_one(data)
    if out!=None:
        try:
            collection.delete_one(data)
            return ({"Meassage":"Data is deleted.",
                      "Success": True,
                      "Status":200})
        except:
            return ({"Meassage":"Something went wrong",
                      "Success": False,
                      "Status":500})
    else:
         return ({"Meassage":"Enter the valid id and username to delete",
                      "Success": True,
                      "Status":200})
    
def update_the_data(data):
    out = collection.find_one(data)
    if out!=None:
        try:
           insert = datetime.now()
           if(out['isPosted']=='no'):
               collection.update_one(data,{"$set":{"isPosted":"yes","postedAt":insert.strftime("%d/%m/%Y %H:%M:%S")}})
               return ({"Meassage":"The article is posted.",
                      "Success": True,
                      "Status":200})
               
           else:
                return ({"Meassage":"The article is already posted.",
                      "Success": True,
                      "Status":200})
               
               
        except:
            return ({"Meassage":"Something went wrong",
                      "Success": False,
                      "Status":500})
    else:
         return ({"Meassage":"Enter the valid id and username to update",
                      "Success": True,
                      "Status":200})
   
    