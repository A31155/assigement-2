from pymongo import MongoClient

client=MongoClient("mongodb+srv://root:1234@cluster0.cbpoe.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

for doc in coll.find():
    print(doc)
    

