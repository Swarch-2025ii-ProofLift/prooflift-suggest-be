import os
from pymongo import MongoClient, ASCENDING, DESCENDING, TEXT

_client = None
_db = None

def get_db():
    global _client, _db
    if _db is None:
        uri = os.getenv("MONGO_URI")
        name = os.getenv("MONGO_DB", "prooflift_suggest")
        if not uri:
            raise RuntimeError("MONGO_URI no está definido")
        _client = MongoClient(uri)
        _db = _client[name]
    return _db

def ensure_indexes():
    col = get_db().exercises
    col.create_index([("group", 1)])
    col.create_index([("muscles", 1)])
    col.create_index([("created_at", -1)])
    col.create_index([("name", "text"), ("synonyms", "text")],
                    name="ex_text", default_language="spanish")
