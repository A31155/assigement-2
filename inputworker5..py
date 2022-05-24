from pymongo import MongoClient

id=int(input('Enter employee ID : '))
nm=input('Enter name : ')
dp=input('Enter department : ')
ps=input('Enter post : ')
sal=int(input('Enter salary : '))
mob=int(input('Enter mobile : '))
ei=input('email id : ')

dic={}
dic["_id"]=id
dic["name"]=nm
dic["dept"]=dp
dic["post"]=ps
dic["salary"]=sal
dic["mobile"]=mob
dic["email id"]=ei

client=MongoClient("mongodb+srv://root:1234@cluster0.cbpoe.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client["office"]
coll=db["workers"]

coll.insert_one(dic)
print('New worker added to MongoDB Collection')
