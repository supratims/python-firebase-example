#https://github.com/thisbejim/Pyrebase
import pyrebase
import FirebaseConfig

config = FirebaseConfig.getConfig()
#print config 
firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()

# Create a new user
email = 'test@phoenix.com'
password = 'password'
auth.create_user_with_email_and_password(email, password)

# Log the user in
user = auth.sign_in_with_email_and_password(email, password)

# Get a reference to the database service
db = firebase.database()

# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}

# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])
