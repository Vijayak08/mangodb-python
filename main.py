import pymongo

#provide mongodb localhost url to connect to python to mongoDB.
client = pymongo.MongoClient('mongodb://localhost:27017')

#Database Name
dataBase=client['testDB']

#collection Name
collection = dataBase['Poducts']

#sample data

d={'company Name': 'AI RealI',
   'product':'Affordabl AI',
   'coursesOffered':'Machine Learning with GenAI'
   }

#Insert above records into collection
rec = collection.insert_one(d)

# lets verify the records

all_records = collection.find()

#printing all records present in the collection

for idx,record in enumerate(all_records):
    print(f"{idx}:{record}")
