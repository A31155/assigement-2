from pymongo import MongoClient

client=MongoClient("mongodb+srv://root:1234@cluster0.cbpoe.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

results=coll.update_one({"_id":102},{"$set":{"salary":99999}})
print("update doc")

for doc in coll.find():
    print(doc)
    

