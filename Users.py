#https://github.com/thisbejim/Pyrebase
import pyrebase
import FirebaseConfig

config = FirebaseConfig.getAdminConfig()
firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

db = firebase.database()
users = db.child("users").get()

for user in users.each():
    print(user.key())
    print(user.val())
