# ProofLift Suggest BE

API (FastAPI + MongoDB) para sugerir / buscar ejercicios.

## Requisitos
- Python 3.11+
- MongoDB en ejecución (local o Atlas)
- pip

## Setup rápido
```bash
# 1. Crear entorno
python -m venv venv
# Activar (Windows PowerShell)
venv\Scripts\Activate.ps1
# (Linux/macOS) source venv/bin/activate

# 2. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 3. Variables (.env) mínimas
# Crear archivo .env con:
# MONGO_URI=mongodb://localhost:27017
# MONGO_DB=prooflift-suggest-db
# FE_ORIGIN=http://localhost:5173

# 4. Seed inicial (opcional la primera vez)
python -c "from app.db.seeds import run; run()"

# 5. Levantar servicio (desarrollo)
uvicorn app:app --reload --port 8000
```

## Endpoints básicos
- GET /health (salud)
- GET /exercises?group=...&q=...&limit=...&cursor=...
- GET /exercises/{id}

## Resumen
1. Crear venv
2. Instalar requirements
3. Configurar .env
4. Seed (solo primera vez)
5. uvicorn app:app --reload --port 8000

Servicio: http://localhost:8000/health
