import pymongo

client = pymongo.MongoClient("mongodb+srv://jean-rafael:lokazo.420@clustercertus.6mvum.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.db_gcp

print(client.list_database_names())