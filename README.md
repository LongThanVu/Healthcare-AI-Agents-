# 🏥 Healthcare A2A System

**Multi-Agent Healthcare Workflow Platform**
Built for **Agents Assemble – The Healthcare AI Endgame**

🔗 [https://agents-assemble.devpost.com/](https://agents-assemble.devpost.com/)

---

## 🚀 Overview

This project is a **production-minded monorepo** that demonstrates a **multi-agent healthcare system (A2A – Agent-to-Agent)** designed to automate and optimize clinical workflows.

The system coordinates **three intelligent agents** through a central **orchestrator**, enabling:

* Faster medical triage decisions
* Automated appointment scheduling
* Efficient patient data retrieval
* Reduced administrative workload

👉 Goal: Build a **scalable, real-world-ready healthcare AI system** for hospitals and clinics.

---

## 🤖 Agents Architecture

### 🧠 Diagnosis Agent

* Analyzes patient symptoms
* Estimates urgency level
* Suggests possible conditions & next steps

### 📅 Scheduling Agent

* Finds available time slots
* Optimizes scheduling
* Books appointments into PostgreSQL

### 📊 Data Agent

* Retrieves patient records from PostgreSQL
* Validates and structures data
* Uses Redis cache for faster search

---

## 🔄 System Flow (A2A Workflow)

1. User logs in via API Gateway
2. User submits symptoms (via dashboard or API)
3. API Gateway validates JWT
4. Request is forwarded to Orchestrator
5. Orchestrator:

   * Fetches patient data (Data Agent)
   * Sends diagnosis request (Diagnosis Agent)
6. Returns unified triage response
7. Optional: Book appointment (Scheduling Agent)

---

## 🧱 Tech Stack

### Backend

* FastAPI
* Pydantic
* SQLAlchemy

### Infrastructure

* PostgreSQL (primary database)
* Redis (caching layer)
* Docker Compose

### Auth

* JWT Authentication

### Frontend

* React + TypeScript + Vite

### Testing

* pytest

---

## 🔐 Authentication Flow

### Register

```
POST /api/v1/auth/register
```

### Login

```
POST /api/v1/auth/login
```

### Get Current User

```
GET /api/v1/auth/me
Authorization: Bearer <token>
```

---

## 🔒 Protected Endpoints

Require JWT token:

* `POST /api/v1/triage`
* `POST /api/v1/appointments/book`
* `POST /api/v1/records/search`

---

## ✨ Key Features

* Multi-agent orchestration (Diagnosis + Scheduling + Data)
* PostgreSQL-backed:

  * Users
  * Patient records
  * Appointments
* Redis caching for record search
* JWT-secured API Gateway
* Clean modular architecture
* Docker-based full-stack setup
* Ready for demo & extension

---

## 📁 Project Structure

```text
healthcare-a2a-system/
├── apps/
│   ├── api-gateway/          # Entry point (REST API + Auth)
│   │   ├── app/
│   │   │   ├── routes/
│   │   │   ├── schemas/
│   │   │   ├── middleware/
│   │   │   └── main.py
│   │   └── tests/
│   │
│   ├── orchestrator/         # Multi-agent coordination
│   │   ├── app/
│   │   │   ├── workflows/
│   │   │   ├── handlers/
│   │   │   ├── protocols/
│   │   │   ├── services/
│   │   │   └── main.py
│   │   └── tests/
│   │
│   └── web-dashboard/        # Frontend UI
│       ├── src/
│       │   ├── pages/
│       │   ├── components/
│       │   ├── services/
│       │   └── hooks/
│       └── tests/
│
├── services/                 # AI Agents
│   ├── diagnosis-agent/
│   │   ├── agent/
│   │   │   ├── diagnosis_agent.py
│   │   │   ├── symptom_analyzer.py
│   │   │   ├── risk_assessor.py
│   │   │   └── recommendation_engine.py
│   │   ├── prompts/
│   │   ├── tools/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── main.py
│   │
│   ├── scheduling-agent/
│   │   ├── agent/
│   │   │   ├── scheduling_agent.py
│   │   │   ├── availability_checker.py
│   │   │   ├── slot_optimizer.py
│   │   │   └── conflict_resolver.py
│   │   ├── tools/
│   │   ├── services/
│   │   └── main.py
│   │
│   └── data-agent/
│       ├── agent/
│       │   ├── data_agent.py
│       │   ├── query_planner.py
│       │   ├── retrieval_engine.py
│       │   └── validation_engine.py
│       ├── repositories/
│       ├── tools/
│       ├── services/
│       └── main.py
│
├── shared/                   # Shared modules
│   ├── core/
│   ├── llm/
│   ├── messaging/
│   ├── database/
│   ├── security/
│   ├── logging/
│   ├── schemas/
│   └── utils/
│
├── configs/
├── docs/
├── tests/
├── scripts/
├── infra/
├── data/
└── README.md
```

---

## ⚙️ Quick Start

### 1. Setup environment

```bash
cp .env.example .env
```

---

### 2. Run system

```bash
docker compose up --build
```

---

### 3. Access services

* API Gateway: [http://localhost:8000/docs](http://localhost:8000/docs)
* Orchestrator: [http://localhost:8001/docs](http://localhost:8001/docs)
* Diagnosis Agent: [http://localhost:8002/docs](http://localhost:8002/docs)
* Scheduling Agent: [http://localhost:8003/docs](http://localhost:8003/docs)
* Data Agent: [http://localhost:8004/docs](http://localhost:8004/docs)
* Web Dashboard: [http://localhost:5173](http://localhost:5173)

---

## 👤 Default Admin Account

* Email: `admin@healthcare.local`
* Password: `admin123456`


