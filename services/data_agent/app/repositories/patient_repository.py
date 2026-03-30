from shared.schemas.records import PatientRecord

PATIENTS = [
    PatientRecord(
        patient_id="P-1001",
        full_name="John Doe",
        age=37,
        gender="male",
        allergies=["penicillin"],
        chronic_conditions=["hypertension"],
        last_visit="2026-03-25",
        notes="Monitor blood pressure and sleep quality.",
    ),
    PatientRecord(
        patient_id="P-1002",
        full_name="Maria Lopez",
        age=29,
        gender="female",
        allergies=[],
        chronic_conditions=["asthma"],
        last_visit="2026-03-18",
        notes="Asthma inhaler prescription renewed.",
    ),
]


class PatientRepository:
    def find_all(self) -> list[PatientRecord]:
        return PATIENTS

    def find_by_id(self, patient_id: str) -> PatientRecord | None:
        return next((patient for patient in PATIENTS if patient.patient_id == patient_id), None)
