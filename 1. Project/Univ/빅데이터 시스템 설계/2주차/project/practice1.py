import pymongo

def main():
    client = pymongo.MongoClient()
    print(client)

    for db in client.list_database_names():
        print(db)

    db_conn = client.get_database("practice")
    print(db_conn)

    for col in db_conn.list_collection_names():
        print(col)

    collection = db_conn.get_collection("students");

    results = collection.find()

    ds = list(results)

    for d in ds:
        print(d)
main()