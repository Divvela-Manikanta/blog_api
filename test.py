from pymongo import MongoClient 


conn = MongoClient("localhost",27017)
db = conn.blog
collection = db.blogcoll


# def insert_data(data):
#     # try:
#         check = collection.find_one({"id":data['id']})
#         if data == None:
#             validate = collection.insert_one(dict(data))
#             return ({"Meassage":"Data is inserted successfully",
#                         "Success": True,
#                         "Status":200})
#         else:
#             return ({"Meassage":"Blogid is already exist.please try with  diffrent blogid.",
#                         "Success": True,
#                         "Status":200})
# data ={"id":"blog2",
# "name":"Best food in hyd",
# "description":"Gives the info about the best foods in hyd",
# "createdBy":"user123",
# "topic":"food",
# "blogBody":"While people can enjoy fine dining at a posh restaurant, the reality is we can’t afford to eat there every day. That’s why readers value advice on how they can make the best food at home. Here are a few meal-specific topics you can blog about to help your target audience do just that ",
# "isPosted":"yes"
# }
        
# insert_data(data)
# data= {"createdBy":"user123"}

# output = collection.aggregate([
#         {"$match":{"createdBy":data['createdBy']}},
#         {"$sort":{"createdAt":-1}},
#         {"$skip":0},
#         {"$limit":9},
#         ]) 
# for val in output:
#     print(val)

# output = collection.aggregate([
#         {"$match":{"isPosted":"yes"}},
#         {"$sort":{"createdAt":-1}},
#         {"$skip":0},
#         {"$limit":9},
#         {"$project":{"name":1,"description":1,"createdBy":1,"postedAt":1}} ]) 
# for val in output:
#     print(val)

def delete_data(data):
    out = collection.find_one(data)
    if out!=0:
        try:
            collection.delete_one(data)
            print ({"Meassage":"Data is deleted.",
                      "Success": True,
                      "Status":200})
        except:
            print ({"Meassage":"Something went wrong",
                      "Success": False,
                      "Status":500})
    else:
         return ({"Meassage":"Enter the valid id and username to delete",
                      "Success": True,
                      "Status":200})

data= {"id":"blog1",
    "createdBy":"user13"}
delete_data(data)