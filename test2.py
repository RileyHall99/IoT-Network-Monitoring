import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

# Initialize Firebase with your service account credentials
cred = credentials.Certificate('test-1-711d6-firebase-adminsdk-mfjte-b60df0f376.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-1-711d6-default-rtdb.firebaseio.com/'
})

# Load the data from your file.json
with open('file.json', 'r') as file:
    data = json.load(file)

# Get a reference to the database
ref = db.reference('/')

# Update the database with the data from file.json
ref.update(data)

print("Data uploaded successfully!")
