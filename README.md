<h2 align="center"><small>ProofLift</small></br> <big>Exercise Suggestion Backend Component</big></h2>

<h5 align="center">Logic Component - Exercise Management Service</br><small>Software Architecture</br>2025-II</small></h5>

---

## 1. Component Overview

**ProofLift Suggest Backend** is a **logic component** in the distributed ProofLift architecture that provides exercise recommendation and search functionality using FastAPI framework and MongoDB as data storage.

### 1.1. Technical Specifications

| Aspect | Technology |
|--------|------------|
| **Programming Language** | Python 3.11+ |
| **Framework** | FastAPI |
| **Database** | MongoDB (NoSQL) |
| **Container** | Docker |

### 1.2. Architectural Role

- **Component Type:** Logic Component
- **Primary Function:** Exercise data management and recommendation
- **Database Type:** NoSQL (MongoDB)

### 1.3. Connectors Used

| Connector Type | Protocol | Purpose |
|----------------|----------|---------|
| **HTTP REST API** | HTTP/HTTPS | Communication with frontend component |
| **Database Connector** | MongoDB Protocol | Data persistence and retrieval |
| **CORS Middleware** | HTTP Headers | Cross-origin resource sharing |

## 2. Project Structure

```
prooflift-suggest-be/
├── app/
│   ├── main.py                     # FastAPI application entry point
│   ├── db/
│   │   ├── mongo.py                # MongoDB connection
│   │   └── seeds.py                # Database seeding
│   ├── models/
│   │   └── exercise.py             # Data models
│   ├── routers/
│   │   └── exercises.py            # API endpoints
│   └── utils/
│       └── pagination.py           # Pagination utilities
├── Dockerfile                      # Container configuration
├── requirements.txt                # Python dependencies
└── .env                           # Environment variables
```

## 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Service health check |
| `GET` | `/exercises` | Search and filter exercises |
| `GET` | `/exercises/{id}` | Get specific exercise details |

## 4. Local Deployment Instructions

### 4.1. Prerequisites

- Python 3.11 or higher
- MongoDB Atlas account (cloud database)
- pip package manager

### 4.2. Environment Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### 4.3. Configuration

Create `.env` file in root directory:
```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/
MONGO_DB=prooflift_suggest
FE_ORIGIN=http://localhost:5173
PORT=8000
```

### 4.4. Database Initialization

```bash
# Seed database with initial exercise data (first time only)
python -c "from app.db.seeds import run; run()"
```

### 4.5. Start Development Server

```bash
# Run with auto-reload
uvicorn app.main:app --reload --port 8000
```

**Service URLs:**
- API Service: http://localhost:8000
- Health Check: http://localhost:8000/health
- API Documentation: http://localhost:8000/docs

### 4.6. Docker Deployment

```bash
# Build container
docker build -t prooflift-suggest-be .

# Run container
docker run -p 8082:8000 --env-file .env prooflift-suggest-be
```

### 4.7. Integration with Complete System

This component integrates with the main ProofLift system via Docker Compose:

```bash
# From project root directory
docker-compose up --build
```

**Exposed Ports:**
- Development: `8000` (internal)
- Production: `8082` (external via Docker)

## 5. Component Integration

### 5.1. Data Flow

1. Frontend sends HTTP requests to `/exercises` endpoints
2. FastAPI processes requests and applies filters
3. MongoDB queries executed with optimized indexes
4. JSON responses returned with pagination metadata

### 5.2. Communication Protocols

- **Inbound:** HTTP REST API from frontend component
- **Outbound:** MongoDB protocol to cloud database
- **Cross-Origin:** CORS headers for web browser security
