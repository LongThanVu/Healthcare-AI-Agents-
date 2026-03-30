import { useState } from "react";
import { postJson } from "./lib/api";

type TriageResponse = {
  patient: { patient_id: string | null; patient_name: string; age: number };
  diagnosis: { condition: string; urgency: string; confidence: number; explanation: string; next_steps: string[] };
  suggested_action: string;
  record_context: unknown;
};

type BookingResponse = {
  appointment_id: string;
  status: string;
  message: string;
  slot: { doctor_name: string; start_time: string; end_time: string; department: string };
};

export default function App() {
  const [triageResult, setTriageResult] = useState<TriageResponse | null>(null);
  const [bookingResult, setBookingResult] = useState<BookingResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleTriageSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);
    const formData = new FormData(event.currentTarget);
    const symptoms = String(formData.get("symptoms") ?? "")
      .split(",")
      .map((value) => value.trim())
      .filter(Boolean);

    try {
      const response = await postJson<TriageResponse>("/api/v1/triage", {
        patient_id: String(formData.get("patient_id") || "") || null,
        patient_name: String(formData.get("patient_name") || "Guest Patient"),
        age: Number(formData.get("age") || 30),
        symptoms,
        notes: String(formData.get("notes") || "") || null,
      });
      setTriageResult(response);
    } catch (submissionError) {
      setError(submissionError instanceof Error ? submissionError.message : "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  async function handleBookingSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);
    setError(null);
    const formData = new FormData(event.currentTarget);

    try {
      const response = await postJson<BookingResponse>("/api/v1/appointments/book", {
        patient_id: String(formData.get("booking_patient_id") || "P-1001"),
        patient_name: String(formData.get("booking_patient_name") || "John Doe"),
        department: String(formData.get("department") || "general-medicine"),
        preferred_date: String(formData.get("preferred_date") || "2026-04-03"),
        urgency: String(formData.get("urgency") || "medium"),
      });
      setBookingResult(response);
    } catch (submissionError) {
      setError(submissionError instanceof Error ? submissionError.message : "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">Healthcare AI • Multi-Agent System</p>
          <h1>Healthcare A2A Dashboard</h1>
          <p className="subtitle">
            Diagnose symptoms, retrieve patient context, and schedule appointments through a coordinated
            multi-agent workflow.
          </p>
        </div>
      </section>

      <div className="grid">
        <section className="card">
          <h2>Triage Patient</h2>
          <form className="form" onSubmit={handleTriageSubmit}>
            <input name="patient_id" placeholder="Patient ID (optional)" />
            <input name="patient_name" placeholder="Patient name" defaultValue="John Doe" />
            <input name="age" type="number" placeholder="Age" defaultValue={37} />
            <input name="symptoms" placeholder="Symptoms (comma separated)" defaultValue="fever, cough" />
            <textarea name="notes" placeholder="Clinical notes" rows={4} />
            <button type="submit" disabled={loading}>{loading ? "Processing..." : "Run triage"}</button>
          </form>
        </section>

        <section className="card">
          <h2>Book Appointment</h2>
          <form className="form" onSubmit={handleBookingSubmit}>
            <input name="booking_patient_id" placeholder="Patient ID" defaultValue="P-1001" />
            <input name="booking_patient_name" placeholder="Patient name" defaultValue="John Doe" />
            <input name="department" placeholder="Department" defaultValue="general-medicine" />
            <input name="preferred_date" placeholder="Preferred date" defaultValue="2026-04-03" />
            <select name="urgency" defaultValue="medium">
              <option value="low">low</option>
              <option value="medium">medium</option>
              <option value="high">high</option>
            </select>
            <button type="submit" disabled={loading}>{loading ? "Processing..." : "Book appointment"}</button>
          </form>
        </section>
      </div>

      {error ? <section className="card error">{error}</section> : null}

      {triageResult ? (
        <section className="card result">
          <h2>Triage Result</h2>
          <p><strong>Condition:</strong> {triageResult.diagnosis.condition}</p>
          <p><strong>Urgency:</strong> {triageResult.diagnosis.urgency}</p>
          <p><strong>Confidence:</strong> {triageResult.diagnosis.confidence}</p>
          <p><strong>Explanation:</strong> {triageResult.diagnosis.explanation}</p>
          <p><strong>Suggested action:</strong> {triageResult.suggested_action}</p>
          <ul>
            {triageResult.diagnosis.next_steps.map((step) => (
              <li key={step}>{step}</li>
            ))}
          </ul>
        </section>
      ) : null}

      {bookingResult ? (
        <section className="card result">
          <h2>Appointment Confirmation</h2>
          <p><strong>Status:</strong> {bookingResult.status}</p>
          <p><strong>Appointment ID:</strong> {bookingResult.appointment_id}</p>
          <p><strong>Doctor:</strong> {bookingResult.slot.doctor_name}</p>
          <p><strong>Department:</strong> {bookingResult.slot.department}</p>
          <p><strong>Time:</strong> {bookingResult.slot.start_time} → {bookingResult.slot.end_time}</p>
          <p>{bookingResult.message}</p>
        </section>
      ) : null}
    </main>
  );
}
