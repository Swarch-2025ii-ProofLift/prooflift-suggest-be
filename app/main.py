from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="ProofLift Suggest API", version="0.1.0")

allowed_origins = [
    os.getenv("FE_ORIGIN", "http://localhost:5173"),
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    from .db.mongo import ensure_indexes
    from .db.seeds import run as run_seeds
    try:
        ensure_indexes()
        run_seeds()
        print("Conectado a MongoDB local")
    except Exception as e:
        print(f"Error conectando a MongoDB: {e}")

@app.get("/health")
def health():
    return {"status": "ok", "database": "local"}

from .routers import exercises
app.include_router(exercises.router)

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
