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
│   ├── api-gateway/
│   │   ├── app/
│   │   │   ├── routes/
│   │   │   ├── schemas/
│   │   │   ├── middleware/
│   │   │   └── main.py
│   │   └── tests/
│   ├── orchestrator/
│   │   ├── app/
│   │   │   ├── workflows/
│   │   │   ├── handlers/
│   │   │   ├── protocols/
│   │   │   ├── services/
│   │   │   └── main.py
│   │   └── tests/
│   └── web-dashboard/
│       ├── public/
│       ├── src/
│       │   ├── pages/
│       │   ├── components/
│       │   ├── services/
│       │   └── hooks/
│       └── tests/
│
├── services/
│   ├── diagnosis-agent/
│   │   ├── app/
│   │   │   ├── agent/
│   │   │   │   ├── diagnosis_agent.py
│   │   │   │   ├── symptom_analyzer.py
│   │   │   │   ├── risk_assessor.py
│   │   │   │   └── recommendation_engine.py
│   │   │   ├── prompts/
│   │   │   │   ├── system_prompt.txt
│   │   │   │   ├── diagnosis_prompt.txt
│   │   │   │   └── explanation_prompt.txt
│   │   │   ├── tools/
│   │   │   │   ├── symptom_checker.py
│   │   │   │   ├── medical_guideline_lookup.py
│   │   │   │   └── triage_tool.py
│   │   │   ├── schemas/
│   │   │   │   ├── request.py
│   │   │   │   ├── response.py
│   │   │   │   └── diagnosis_result.py
│   │   │   ├── services/
│   │   │   │   ├── diagnosis_service.py
│   │   │   │   └── confidence_service.py
│   │   │   └── main.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   ├── integration/
│   │   │   └── evaluation/
│   │   └── README.md
│   │
│   ├── scheduling-agent/
│   │   ├── app/
│   │   │   ├── agent/
│   │   │   │   ├── scheduling_agent.py
│   │   │   │   ├── availability_checker.py
│   │   │   │   ├── slot_optimizer.py
│   │   │   │   └── conflict_resolver.py
│   │   │   ├── prompts/
│   │   │   │   ├── system_prompt.txt
│   │   │   │   ├── booking_prompt.txt
│   │   │   │   └── reschedule_prompt.txt
│   │   │   ├── tools/
│   │   │   │   ├── doctor_calendar_tool.py
│   │   │   │   ├── patient_notification_tool.py
│   │   │   │   └── appointment_validator.py
│   │   │   ├── schemas/
│   │   │   │   ├── booking_request.py
│   │   │   │   ├── booking_response.py
│   │   │   │   └── appointment_slot.py
│   │   │   ├── services/
│   │   │   │   ├── booking_service.py
│   │   │   │   └── reminder_service.py
│   │   │   └── main.py
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   ├── integration/
│   │   │   └── evaluation/
│   │   └── README.md
│   │
│   └── data-agent/
│       ├── app/
│       │   ├── agent/
│       │   │   ├── data_agent.py
│       │   │   ├── query_planner.py
│       │   │   ├── retrieval_engine.py
│       │   │   └── validation_engine.py
│       │   ├── prompts/
│       │   │   ├── system_prompt.txt
│       │   │   ├── retrieval_prompt.txt
│       │   │   └── validation_prompt.txt
│       │   ├── tools/
│       │   │   ├── sql_tool.py
│       │   │   ├── patient_record_tool.py
│       │   │   └── vector_search_tool.py
│       │   ├── repositories/
│       │   │   ├── patient_repository.py
│       │   │   ├── appointment_repository.py
│       │   │   └── medical_history_repository.py
│       │   ├── schemas/
│       │   │   ├── query_request.py
│       │   │   ├── query_response.py
│       │   │   └── patient_record.py
│       │   ├── services/
│       │   │   ├── retrieval_service.py
│       │   │   └── data_access_service.py
│       │   └── main.py
│       ├── tests/
│       │   ├── unit/
│       │   ├── integration/
│       │   └── evaluation/
│       └── README.md
│
├── shared/
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
│   ├── app/
│   ├── agents/
│   ├── prompts/
│   └── logging/
│
├── docs/
│   ├── architecture/
│   ├── api/
│   ├── workflow/
│   └── deployment/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   └── performance/
│
├── scripts/
│   ├── setup_local.sh
│   ├── seed_data.py
│   ├── run_tests.sh
│   └── migrate_db.sh
│
├── infra/
│   ├── docker/
│   ├── k8s/
│   └── ci-cd/
│
├── data/
│   ├── sample/
│   ├── fixtures/
│   └── mock/
│
└── README.md
