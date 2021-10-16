from flask import *
from conn import *
from bson import json_util

app=Flask(__name__)

mydb=mongoConnect()

@app.route('/user',methods=['POST'])
def create_user():
    mycol=mydb["users"]
    username=request.json['username']
    age=request.json['age']
    q=request.json['qualificarion']
    data={
        "username":username,
        'age':age,
        'qualification':q
    }
    x=mycol.insert_one(data)

    response={
        "id":str(x.inserted_id),
        "username":username,
        'age':age,
        'qualification':q
    }
    return response

@app.route('/user',methods=['GET'])
def all_user():
    mycol=mydb["users"]
    users=mycol.find()
    response=json_util.dumps(users)
    return response

@app.route('/user/<name>',methods=['GET'])
def single_user(name):
    mycol=mydb["users"]
    users=mycol.find_one({
        "username": name
    })
    response=json_util.dumps(users)
    return response

@app.route('/user/<name>',methods=['DELETE'])
def delete_user(name):
    mycol=mydb["users"]
    users=mycol.delete_one({
        "username": name
    })
    return jsonify({"Message" :name+" is Deleted"})

@app.route('/user/<name>',methods=['PUT'])
def update_user(name):
    mycol=mydb["users"]
    username=request.json['username']
    age=request.json['age']
    q=request.json['qualificarion']

    data={
        "username":username,
        'age':age,
        'qualification':q
    }
    mycol.update_one({"username":name},{"$set":data})
    return jsonify({"Message" :name+" is Updated"})


if __name__=='__main__':
    app.run(debug=True)