from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient, ASCENDING, DESCENDING, TEXT
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="ProofLift Suggest API", version="0.1.0")

# CORS: ajusta el origin a tu FE
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FE_ORIGIN","http://localhost:5173")],
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB","prooflift-suggest-db")]

def ensure_indexes():
    col = db.exercises
    col.create_index([("muscles", ASCENDING)])
    col.create_index([("goal_tags", ASCENDING)])
    col.create_index([("created_at", DESCENDING)])
    col.create_index([("name", TEXT), ("synonyms", TEXT)], name="ex_text")

@app.on_event("startup")
def on_startup():
    ensure_indexes()

@app.get("/health")
def health(): return {"status": "ok"}
