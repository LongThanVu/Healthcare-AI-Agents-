from services.data_agent.app.repositories.patient_repository import PATIENTS

for patient in PATIENTS:
    print(patient.model_dump())
