import firebase_admin
from firebase_admin import credentials, firestore
import json

# Initialize Firebase Admin SDK
cred = credentials.Certificate('test-1-711d6-firebase-adminsdk-mfjte-b60df0f376.json')
firebase_admin.initialize_app(cred)

# Specify the path to your JSON file
json_file_path = 'file.json'

# Load JSON data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Specify the Firestore collection where you want to upload the data
collection_name = 'test-1'

# Get a reference to the Firestore database
db = firestore.client()

# Upload data to Firebase Firestore
for item in data:
    db.collection(collection_name).add(item)

print('Data uploaded successfully!')
