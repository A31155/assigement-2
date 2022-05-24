from pymongo import MongoClient

client=MongoClient("mongodb+srv://root:1234@cluster0.cbpoe.mongodb.net/office?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

code=int(input('Enter worker ID : '))
qr={}
qr["_id"]=code
print(qr)

for doc in coll.find(qr):
    print(doc)
