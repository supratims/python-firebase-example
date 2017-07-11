### Simple firebase usage from python 
* Uses pyrebase : https://github.com/thisbejim/Pyrebase

### Firebase : Mobile backend as a service from google
* Create a new account and get keys from https://console.firebase.google.com
* Make sure you email/password enabled as sign in methods in firebase
	Check under Console->Authentication->Sign-inMethods 
* Save api keys (for user sign in etc) , from Project Settings (click on cog near overview) -> General -> Click Add Firebase to your web app. Save keys as key value pair in api.keys file. See `FirebaseConfig.py`
* Save service account (admin) keys from Project Settings -> Service Accounts -> Generate New private key . And save down the json as  python-tester-service_account_credentials.json 

### Installation

* Install pyrebase - the client to connect to firebase usign python
	`pip install pyrebase`

### Usage
* Create user: Creates a new user in firebase , uses hardcoded email and password in script for the user to create
	`python CreateUser.py`

* List user: Lists the users in your firebase database, uses service account credentials
	`python Users.py`

