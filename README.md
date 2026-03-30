# Healthcare A2A System

A clean, production-minded monorepo for a multi-agent healthcare workflow platform built for **Agents Assemble – The Healthcare AI Endgame**.

## Overview

This system uses three specialized agents coordinated through an orchestrator:

- **Diagnosis Agent**: analyzes symptoms, estimates urgency, and suggests next actions.
- **Scheduling Agent**: proposes and books appointments into PostgreSQL-backed storage.
- **Data Agent**: retrieves patient records from PostgreSQL and caches search results in Redis.

The API Gateway now includes **JWT authentication**, so core workflows are protected and ready for a more realistic product demo.

## Tech Stack

- **Backend**: FastAPI, Pydantic, SQLAlchemy
- **Database**: PostgreSQL
- **Cache**: Redis
- **Auth**: JWT
- **Frontend**: React + TypeScript + Vite
- **Infra**: Docker Compose
- **Testing**: pytest

## Key Features

- Multi-agent orchestration for triage, scheduling, and record lookup
- PostgreSQL-backed users, patient records, and appointments
- Redis cache for patient record search
- JWT auth with `register`, `login`, and `me` endpoints
- Protected workflow endpoints on the API Gateway
- Docker Compose for local full-stack development

## Project Structure

```text
healthcare-a2a-system/
├── apps/
│   ├── api-gateway/
│   ├── orchestrator/
│   └── web-dashboard/
├── services/
│   ├── diagnosis-agent/
│   ├── scheduling-agent/
│   └── data-agent/
├── shared/
├── configs/
├── docs/
├── tests/
├── scripts/
├── infra/
├── data/
└── README.md
```

## Quick Start

### 1. Copy environment variables

```bash
cp .env.example .env
```

### 2. Run with Docker Compose

```bash
docker compose up --build
```

### 3. Open services

- API Gateway: `http://localhost:8000/docs`
- Orchestrator: `http://localhost:8001/docs`
- Diagnosis Agent: `http://localhost:8002/docs`
- Scheduling Agent: `http://localhost:8003/docs`
- Data Agent: `http://localhost:8004/docs`
- Web Dashboard: `http://localhost:5173`

## Default Seeded Admin

- **Email**: `admin@healthcare.local`
- **Password**: `admin123456`

You can change these values in `.env` before startup.

## Auth Flow

### Register

```http
POST /api/v1/auth/register
```

### Login

```http
POST /api/v1/auth/login
```

### Current User

```http
GET /api/v1/auth/me
Authorization: Bearer <token>
```

## Protected Workflow Endpoints

All endpoints below require a Bearer token:

- `POST /api/v1/triage`
- `POST /api/v1/appointments/book`
- `POST /api/v1/records/search`

## Example Workflow

1. User logs in through the API Gateway.
2. User submits symptoms through the dashboard.
3. API Gateway validates JWT and forwards the request to the orchestrator.
4. The orchestrator requests patient context from the Data Agent.
5. The orchestrator sends a diagnosis request to the Diagnosis Agent.
6. The orchestrator returns a unified triage response.
7. If needed, the user can book an appointment through the Scheduling Agent.

## Notes

- This is still a starter project, not a hospital-grade compliance implementation.
- It is intentionally clean and compact so it is easy to present, demo, and extend.
