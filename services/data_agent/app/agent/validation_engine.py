from shared.schemas.records import PatientRecord


class ValidationEngine:
    @staticmethod
    def validate(record: PatientRecord) -> PatientRecord:
        return record
