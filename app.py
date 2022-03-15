config = {
    "apiKey": "AIzaSyDh2fn6QMGcDBaP7_DlwrDUngg9Xr1V0mw",
    "authDomain": "bankingappbyaj.firebaseapp.com",
    "databaseURL": "https://bankingappbyaj-default-rtdb.firebaseio.com",
    "projectId": "bankingappbyaj",
    "storageBucket": "bankingappbyaj.appspot.com",
    "messagingSenderId": "609572537357",
    "appId": "1:609572537357:web:655ed1404976ed3fc68144",
    "measurementId": "G-E8H7F5QQYX"
  }




from flask import Flask 
import json
import Model



import pyrebase
# firebase = pyrebase.initialize_app(config)
# db = firebase.database()
# storage = firebase.storage()
# user = db.child("images").get()

# all_users = db.child("images").get()
# #print(len(all_users))
# for user in all_users.each():
#     key = user.key()
#     arr = user.val()
    
#     if arr["read"] == False:
#         print("1")
#         path1 = arr["images"]
#         print("2")
#         db.child("images"+"/"+key).set(
#             {"images":path1,
#             "read":True
#             }
#             )
        
#         print("3")
#         storage.child("images/"+path1).download("H:/DatabaseData/"+path1)
#         print("4")
#         print(path1)
#     else:
#         pass




app=Flask(__name__)
# app.run(debug=True)

@app.route('/members')
# @app.route('/')

def members():
    global path1
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    storage = firebase.storage()
    user = db.child("images_formodel").get()
    all_users = db.child("images_formodel").get()
    #print(len(all_users))
    for user in all_users.each():
        key = user.key()
        arr = user.val()
        if arr["read"] == False:
            
            path1 = arr["image"]

            db.child("images_formodel"+"/"+key).set(
            {"image":path1,
            "read":True
            }
            )
            storage.child("images_formodel/"+path1).download("H:/DatabaseData/Input/"+path1)
           
        else:
            pass
    print(path1,"path1")
    severity,hist=Model.XrayAnalyzer("H:/DatabaseData/Input/"+path1)
    return {
        
        "Severity":severity,
        "Histogram":hist
        
    }


if __name__=='__main__':

    app.run(debug=True)
