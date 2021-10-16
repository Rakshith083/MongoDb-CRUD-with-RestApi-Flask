import pymongo

def mongoConnect():
    conString="mongodb://localhost:27017/Rest"
    try:
        myclient = pymongo.MongoClient(conString)
        print("connected")
    except:
        print("Unable to connect")

    mydb = myclient["Rest"]
    return mydb