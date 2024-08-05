from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:brettfavre4@cluster0.j3ebv0r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Get the database using the method we defined in pymongo_test_insert file
 
# Retrieve a collection named "user_1_items" from database
collection_name = client["sample_mflix"]["comments"]
 
item_details = collection_name.find()
for item in item_details:
   print(item)