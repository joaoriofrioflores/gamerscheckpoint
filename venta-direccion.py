#trabajando...
import pymongo

client = pymongo.MongoClient("mongodb+srv://jean-rafael:lokazo.420@clustercertus.6mvum.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.db_gcp

coll = db.users

coll.insert_many([
    {'nombre':'Lokazo thc',
    'apellidos':'Cuatro Veinte',
    'provincia':'Lima',
    'distrito':'Breña',
    'calle':'Jr. Marhihuana',
    'numero':'420',
    'interior':'666',
    'telefonos':['992453123', '929351202']},
    {'nombre':'Anacleto Cocaina',
    'apellidos':'Sopota Madre',
    'provincia':'Tacna',
    'distrito':'Miraflores',
    'calle':'Jr. LSD',
    'numero':'69',
    'interior':'420',
    'telefonos':['999555333', '988977344']}
])

for documento in coll.find({

})

print(client.list_database_names())