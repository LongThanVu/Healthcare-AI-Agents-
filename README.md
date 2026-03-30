# 🏥 Healthcare AI Agents
This repository is created for the competition:
**Agents Assemble – The Healthcare AI Endgame**
---
Competition link: 
🔗 [https://agents-assemble.devpost.com/](https://agents-assemble.devpost.com/)
### 👥 Team Project
We build an A2A system with three intelligent agents working together:

* **Agent 1:** Handles disease diagnosis
* **Agent 2:** Manages patient scheduling
* **Agent 3:** Checks and retrieves data from the database

This system is designed to streamline healthcare workflows by automating key processes. It helps doctors make faster decisions, reduces administrative workload, and improves patient experience.

By combining multiple AI agents, the system enables more efficient, accurate, and scalable healthcare solutions that can support hospitals and clinics in real-world scenarios.

healthcare-a2a-system/
├── apps/
│   ├── api-gateway/          # Entry point for client requests (REST/API)
│   │   ├── app/
│   │   │   ├── routes/       # API endpoints
│   │   │   ├── schemas/      # Request/response models
│   │   │   ├── middleware/   # Auth, logging, rate limit
│   │   │   └── main.py
│   │   └── tests/
│
│   ├── orchestrator/        # A2A coordination between agents
│   │   ├── app/
│   │   │   ├── workflows/    # Multi-agent workflows
│   │   │   ├── handlers/     # Agent-specific handlers
│   │   │   ├── protocols/    # Message formats (A2A)
│   │   │   ├── services/     # Orchestration logic
│   │   │   └── main.py
│   │   └── tests/
│
│   └── web-dashboard/       # Frontend for doctors/admin
│       ├── public/
│       ├── src/
│       │   ├── pages/
│       │   ├── components/
│       │   ├── services/
│       │   └── hooks/
│       └── tests/
│
├── services/                # Independent AI agents
│   ├── diagnosis-agent/     # Agent 1: Disease diagnosis
│   │   ├── app/
│   │   │   ├── agent/        # Core reasoning logic
│   │   │   │   ├── diagnosis_agent.py
│   │   │   │   ├── symptom_analyzer.py
│   │   │   │   ├── risk_assessor.py
│   │   │   │   └── recommendation_engine.py
│   │   │   ├── prompts/      # LLM prompts
│   │   │   ├── tools/        # External tools (guidelines, symptom checker)
│   │   │   ├── schemas/      # Input/output formats
│   │   │   ├── services/     # Business logic layer
│   │   │   └── main.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   ├── integration/
│   │   │   └── evaluation/
│   │   └── README.md
│
│   ├── scheduling-agent/    # Agent 2: Appointment scheduling
│   │   ├── app/
│   │   │   ├── agent/
│   │   │   │   ├── scheduling_agent.py
│   │   │   │   ├── availability_checker.py
│   │   │   │   ├── slot_optimizer.py
│   │   │   │   └── conflict_resolver.py
│   │   │   ├── prompts/
│   │   │   ├── tools/        # Calendar, notifications
│   │   │   ├── schemas/
│   │   │   ├── services/
│   │   │   └── main.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   ├── integration/
│   │   │   └── evaluation/
│   │   └── README.md
│
│   └── data-agent/          # Agent 3: Data retrieval & validation
│       ├── app/
│       │   ├── agent/
│       │   │   ├── data_agent.py
│       │   │   ├── query_planner.py
│       │   │   ├── retrieval_engine.py
│       │   │   └── validation_engine.py
│       │   ├── prompts/
│       │   ├── tools/        # SQL, vector search
│       │   ├── repositories/ # DB access layer
│       │   ├── schemas/
│       │   ├── services/
│       │   └── main.py
│       ├── tests/
│       │   ├── unit/
│       │   ├── integration/
│       │   └── evaluation/
│       └── README.md
│
├── shared/                 # Shared modules across services
│   ├── core/               # Config, constants
│   ├── llm/                # LLM abstraction layer
│   ├── messaging/          # Event/message system
│   ├── database/           # DB models & session
│   ├── security/           # Auth, encryption
│   ├── logging/            # Logging & tracing
│   ├── schemas/            # Shared data models
│   └── utils/              # Helper functions
│
├── configs/                # Environment & system configs
│   ├── app/
│   ├── agents/
│   ├── prompts/
│   └── logging/
│
├── docs/                   # Project documentation
│   ├── architecture/
│   ├── api/
│   ├── workflow/
│   └── deployment/
│
├── tests/                  # Global test suite
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── performance/
│
├── scripts/                # Utility scripts
│   ├── setup_local.sh
│   ├── seed_data.py
│   ├── run_tests.sh
│   └── migrate_db.sh
│
├── infra/                  # Deployment & DevOps
│   ├── docker/
│   ├── k8s/
│   └── ci-cd/
│
├── data/                   # Sample & mock data
│   ├── sample/
│   ├── fixtures/
│   └── mock/
│
└── README.md
